import axios from 'axios';
import { api } from 'boot/axios';
import { useQuasar } from 'quasar';

const $q = useQuasar();
const TOKEN_KEY = 'aTkn';
const REFRESH_TOKEN_KEY = 'rTkn';

export function getToken() {
  return localStorage.getItem(TOKEN_KEY);
}

export function setToken(token) {
  localStorage.setItem(TOKEN_KEY, token);
  localStorage.setItem('ts', Date.now());
}

export function getRefreshToken() {
  return $q.cookies.get(REFRESH_TOKEN_KEY);
}

export function setRefreshToken(refreshToken) {
  $q.cookies.set(REFRESH_TOKEN_KEY, refreshToken, { path: '/', secure: false, httpOnly: true, sameSite: 'Strict', expires: new Date(Date.now() + 1000 * 60 * 60 * 24) });
  $q.cookies.set('ts', Date.now(), { path: '/', secure: false, httpOnly: true, sameSite: 'Strict', expires: new Date(Date.now() + 1000 * 60 * 60 * 24) });
}

export function getTimestampRefreshToken(){
    return $q.cookies.get('ts');
}

export function getTimestampToken(){
    return localStorage.getItem('ts');
}

export function removeTokens() {
  localStorage.removeItem(TOKEN_KEY);
  $q.cookies.remove(REFRESH_TOKEN_KEY);
}

export function isTokenExpired(token, ts, tl) {
  if (!token) return true;

  const now = Date.now();
  const diff = now - ts;

  // Here is the life time of the tokens
  // CHANGE IN THE FUTURE: FIX
  let lifeTime = 0;
  if(tl == '1d'){
    lifeTime = 1000 * 60 * 60 * 24;
  }else if(tl == '15m'){
    lifeTime = 1000 * 60 * 15;
  }

  if(diff >= lifeTime) return true;
  return false;
}

export async function refreshToken() {
  try {
    const refreshToken = getRefreshToken();
    const response = await api.post('/token/refresh-token/', { refreshToken });
    const { accessToken, refreshToken: newRefreshToken } = response.data;
    setToken(accessToken);
    setRefreshToken(newRefreshToken);
    return accessToken;
  } catch (error) {
    console.error('Error refreshing token:', error);
    removeTokens();
    throw error;
  }
}

export async function getValidToken() {
  let token = getToken();
  if (isTokenExpired(token)) {
    token = await refreshToken();
  }
  return token;
}