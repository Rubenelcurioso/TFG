import { defineStore } from 'pinia';

export const useCounterStore = defineStore('counter', {
  state: () => ({
    id: null,
    username: '',
    projects: [],
  }),
  getters: {
    userId: (state) => state.id,
    userName: (state) => state.username,
    userProjects: (state) => state.projects,
  },
  actions: {
    setUser(user) {
      this.id = user.id;
      this.username = user.username;
    },
    setProjects(projects) {
      this.projects = projects;
    },
  },
});
