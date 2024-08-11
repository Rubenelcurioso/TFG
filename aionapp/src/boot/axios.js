import { boot } from 'quasar/wrappers'
import axios from 'axios'
import { useQuasar } from 'quasar'
import { useRouter } from 'vue-router'

// Be careful when using SSR for cross-request state pollution
// due to creating a Singleton instance here;
// If any client changes this (global) instance, it might be a
// good idea to move this instance creation inside of the
// "export default () => {}" function below (which runs individually
// for each client)
const api = axios.create({ baseURL: 'http://localhost:8000/' })

export default boot(({ app }) => {
  // for use inside Vue files (Options API) through this.$axios and this.$api


  const $q = useQuasar()
  const router = useRouter()
  // Add interceptor
  app.config.globalProperties.$axios = axios
  // ^ ^ ^ this will allow you to use this.$axios (for Vue Options API form)
  //       so you won't necessarily have to import axios in each vue file

  app.config.globalProperties.$api = api
  // ^ ^ ^ this will allow you to use this.$api (for Vue Options API form)
  //       so you can easily perform requests against your app's API

    /*api.interceptors.request.use(
    async (config) => {
      const token = localStorage.getItem('aTkn');
      if (token) {
        config.headers['Authorization'] = `Bearer ${token}`;
      }

      // Check if token is expired
      if (isTokenExpired(token)) {
        try {
          const response = await refreshToken();
          const expirationDate = new Date();
          expirationDate.setDate(expirationDate.getDate() + 1);
          $q.cookies.set('rTkn', response.data.refresh_token,{ path: '/', secure: false, httpOnly: true, sameSite: 'Strict', expires: expirationDate });
          localStorage.setItem('aTkn', response.data.access_token);
          localStorage.setItem('ts', Date.now());
          config.headers['Authorization'] = `Bearer ${response.data.access_token}`;
        } catch (error) {
          // Handle refresh token failure (e.g., redirect to login)
          console.error('Failed to refresh token:', error);
          router.push('/login');
        }
      }

      return config;
    },
    (error) => {
      return Promise.reject(error);
    }
  );*/
})

export { axios, api }

// Helper function to check if token is expired
function isTokenExpired(token) {
  if (!token) return true;

  // Check the localStorage timestamp 
  const ts = localStorage.getItem('ts');
  const now = Date.now();
  const diff = now - ts;
  // Check diff is 15 minutes or greater
  if(diff >= 15 * 60 * 1000) return true;

  return false;
}

// Function to refresh token
async function refreshToken() {
  const refreshToken = localStorage.getItem('refreshToken');
  const response = await api.post('/token/refresh/', { refreshToken });
  return response;
}
