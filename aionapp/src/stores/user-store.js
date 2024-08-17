import { defineStore } from 'pinia';

export const useUserStore = defineStore('user', {
  state: () => ({
    uid: 0,
    username: '',
    projects: [],
  }),
  getters: {
    userId: (state) => state.uid,
    userName: (state) => state.username,
    userProjects: (state) => state.projects,
  },
  actions: {
    setUser(user) {
      this.uid = user.uid;
      this.username = user.username;
    },
    setProjects(projects) {
      this.projects = projects;
    },
  },
});
