const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/LandscapePage.vue') }
    ]
  },

  {
    path: '/register',
    component: () => import('layouts/MainLayout.vue'),
    children:  [
      { path: '', component: () => import('pages/RegisterPage.vue') }
    ]
  },

  {
    path: '/login',
    component: () => import('layouts/MainLayout.vue'),
    children:  [
      { path: '', component: () => import('pages/LoginPage.vue') }
    ]
  },

  {
    path: '/home/:uid',
    component: () => import('layouts/LoggedLayout.vue'),
    children:  [
      { path: '', component: () => import('pages/HomeUser.vue') }
    ]
  },


  {
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
