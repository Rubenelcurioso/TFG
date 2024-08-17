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
    setProjects(project) {
      const existingProject = this.projects.find(p => p.id === project.id)
      
      if (!existingProject) {
        this.projects.push(project)
      } else {
        const updatedFields = ['name', 'description', 'start_date', 'end_date', 'progress']
        
        updatedFields.forEach(field => {
          if (existingProject[field] !== project[field]) {
            existingProject[field] = project[field]
          }
        })
      }
    },
  },
  persist: {
    storage: sessionStorage
  }
});
