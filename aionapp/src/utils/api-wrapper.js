import { api } from 'boot/axios';
import { getValidToken } from './token-management';

/**
 * Sends a GET request to the specified URL with the provided configuration.
 *
 * @param {string} url - The URL to send the GET request to.
 * @param {object} [config={}] - The configuration object for the request.
 * @param {object} [config.headers] - Additional headers to include in the request.
 * @returns {Promise<any>} - The response data from the API.
 */
export async function apiGet(url, config = {}) {
  try {
    const token = await getValidToken();
    const response = await api.get(url, {
      ...config,
      headers: {
        ...config.headers,
        Authorization: `Bearer ${token}`
      }
    });
    return response.data;
  } catch (error) {
    handleApiError(error);
  }
}


/**
 * Sends a POST request to the specified URL with the provided data and configuration.
 *
 * @param {string} url - The URL to send the POST request to.
 * @param {object} data - The data to include in the POST request body.
 * @param {object} [config={}] - The configuration object for the request.
 * @param {object} [config.headers] - Additional headers to include in the request.
 * @returns {Promise<any>} - The response data from the API.
 */
export async function apiPost(url, data, config = {}) {
  try {
    const headers = { ...config.headers };
    if (url !== '/register/' && url !== '/login/') {
      const token = await getValidToken();
      headers.Authorization = `Bearer ${token}`;
    }
    const response = await api.post(url, data, {
      ...config,
      headers
    });
    return response.data;
  } catch (error) {
    handleApiError(error);
  }
}

/**
 * Sends a PUT request to the specified URL with the provided data and configuration.
 *
 * @param {string} url - The URL to send the PUT request to.
 * @param {object} data - The data to include in the PUT request body.
 * @param {object} [config={}] - The configuration object for the request.
 * @param {object} [config.headers] - Additional headers to include in the request.
 * @returns {Promise<any>} - The response data from the API.
 */
export async function apiPut(url, data, config = {}) {
  try {
    const token = await getValidToken();
    const response = await api.put(url, data, {
      ...config,
      headers: {
        ...config.headers,
        Authorization: `Bearer ${token}`
      }
    });
    return response.data;
  } catch (error) {
    handleApiError(error);
  }
}

/**
 * Sends a DELETE request to the specified URL with the provided configuration.
 *
 * @param {string} url - The URL to send the DELETE request to.
 * @param {object} [config={}] - The configuration object for the request.
 * @param {object} [config.headers] - Additional headers to include in the request.
 * @returns {Promise<any>} - The response data from the API.
 */
export async function apiDelete(url, config = {}) {
  try {
    const token = await getValidToken();
    const response = await api.delete(url, {
      ...config,
      headers: {
        ...config.headers,
        Authorization: `Bearer ${token}`
      }
    });
    return response.data;
  } catch (error) {
    handleApiError(error);
  }
}

/**
 * Handles API errors by logging the error details and throwing the error.
 *
 * @param {Error} error - The error object containing information about the API request failure.
 * @throws {Error} - The original error object.
 */
function handleApiError(error) {
  if (error.response) {
    // The request was made and the server responded with a status code
    // that falls out of the range of 2xx
    console.error('API Error:', error.response.data);
    console.error('Status:', error.response.status);
    console.error('Headers:', error.response.headers);
  } else if (error.request) {
    // The request was made but no response was received
    console.error('No response received:', error.request);
  } else {
    // Something happened in setting up the request that triggered an Error
    console.error('Error setting up request:', error.message);
  }
  throw error;
}