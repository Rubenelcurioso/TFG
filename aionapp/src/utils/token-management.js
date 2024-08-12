import { api } from 'boot/axios';
import { useRouter } from 'vue-router';
import { Cookies } from 'quasar'
import { LocalStorage } from 'quasar';


const router = useRouter();
const TOKEN_KEY = 'aTkn';
const REFRESH_TOKEN_KEY = 'rTkn';

/**
 * Gets the access token stored in the local storage.
 *
 * @returns {string} The access token.
 */
export function getToken() {
  return LocalStorage.getItem(TOKEN_KEY);
}

/**
 * Sets the access token and the timestamp when the access token was set.
 *
 * @param {string} token - The access token to be stored.
 */
export function setToken(token) {
  LocalStorage.set(TOKEN_KEY, token);
  LocalStorage.set('ts', Date.now());
}

export function getRefreshToken() {
  return Cookies.get(REFRESH_TOKEN_KEY);
}

/**
 * Sets the refresh token and the timestamp when the refresh token was set.
 *
 * @param {string} refreshToken - The refresh token to be stored.
 */
export function setRefreshToken(refreshToken) { // Change here Cookie secure when get the HTTPS certs
  Cookies.set(REFRESH_TOKEN_KEY, refreshToken, { path: '/', secure: false, httpOnly: true, sameSite: 'Strict', expires: new Date(Date.now() + 1000 * 60 * 60 * 24) });
  Cookies.set('ts', Date.now(), { path: '/', secure: false, httpOnly: true, sameSite: 'Strict', expires: new Date(Date.now() + 1000 * 60 * 60 * 24) });
}

/**
 * Gets the timestamp when the refresh token was set.
 *
 * @returns {number} The timestamp (in milliseconds) when the refresh token was set.
 */
export function getTimestampRefreshToken(){
    return Cookies.get('ts');
}

/**
 * Gets the timestamp when the access token was set.
 *
 * @returns {number} The timestamp (in milliseconds) when the access token was set.
 */
export function getTimestampToken(){
    return LocalStorage.getItem('ts');
}

/**
 * Removes the stored access token and refresh token.
 * This function should be called when the user logs out or the tokens are no longer valid.
 */
export function removeTokens() {
  LocalStorage.clear();
  Cookies.remove(REFRESH_TOKEN_KEY);
  Cookies.remove('ts');
}

/**
 * Checks if a given token has expired based on the provided timestamp and lifetime.
 *
 * @param {string} token - The token to check for expiration.
 * @param {number} ts - The timestamp (in milliseconds) when the token was issued.
 * @param {string} tl - The lifetime of the token, either '1d' for 1 day or '15m' for 15 minutes.
 * @returns {boolean} `true` if the token has expired, `false` otherwise.
 */
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


/**
 * Refreshes the access token using the stored refresh token.
 *
 * This function first checks if the stored refresh token is still valid. If so, it makes a request to the server to obtain a new access token and refresh token. The new tokens are then stored in the appropriate storage locations.
 *
 * If the refresh token is expired, this function removes the stored tokens and redirects the user to the login page.
 *
 * @returns {Promise<string>} The new access token, redirects to the login page if the refresh token is expired.
 */
export async function refreshToken() {
  try {
    const refreshToken = getRefreshToken();
    if(!isTokenExpired(refreshToken, getTimestampRefreshToken(), '1d')){
      const response = await api.post('/token/refresh/', { refreshToken });
      const { accessToken, refreshToken: newRefreshToken } = response.data;
      setToken(response.data.access_token);
      setRefreshToken(response.data.refresh_token);
      return accessToken;
    }else{
      removeTokens();
      router.push('/login');
      throw new Error('Tokens expired, redirected to login');
    }
  } catch (error) {
    console.error('Error refreshing token:', error);
    removeTokens();
    throw error;
  }
}

/**
 * Retrieves a valid access token, refreshing it if necessary.
 *
 * This function first attempts to retrieve the current access token from storage.
 * If the token is expired, it calls the `refreshToken()` function to obtain a new
 * access token using the stored refresh token.
 *
 * @returns {Promise<string>} A valid access token or null if the refresh token is expired.
 */
export async function getValidToken() {
  let token = getToken();
  if (isTokenExpired(token)) {
    token = await refreshToken();
  }
  return token;
}