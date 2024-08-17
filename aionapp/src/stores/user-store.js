import { defineStore } from 'pinia';

export const useCounterStore = defineStore('counter', {
  state: () => ({
    id: null,
    username: '',
  }),
  getters: {
    // No longer needed, can be removed or commented out
  },
  actions: {
    setUser(user) {
      this.id = user.id;
      this.username = user.username;
    },
  },
});
