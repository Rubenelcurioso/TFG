import { isTokenExpired, getRefreshToken, getTimestampRefreshToken } from 'src/utils/token-management';

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
    path: '/privacy-policy',
    component: () => import('layouts/MainLayout.vue'),
    children:  [
      { path: '', component: () => import('pages/PrivacyPoliticsPage.vue') }
    ]
  },

  {
    path: '/contact',
    component: () => import('layouts/MainLayout.vue'),
    children:  [
      { path: '', component: () => import('pages/ContactPage.vue') }
    ]
  },

  {
    path: '/about-us',
    component: () => import('layouts/MainLayout.vue'),
    children:  [
      { path: '', component: () => import('pages/AboutUsPage.vue') }
    ]
  },

  {
    path: '/security-best-practices',
    component: () => import('layouts/MainLayout.vue'),
    children:  [
      { path: '', component: () => import('pages/SecurityBestPracticesPage.vue') }
    ]
  },

  {
    path: '/our-mission',
    component: () => import('layouts/MainLayout.vue'),
    children:  [
      { path: '', component: () => import('pages/OurMissionPage.vue') }
    ]
  },

  {
    path: '/home/:uid',
    component: () => import('layouts/LoggedLayout.vue'),
    meta: { requiresAuth: true },
    beforeEnter: (to, from, next) => {
      if (isTokenExpired(getRefreshToken(), getTimestampRefreshToken(), '1d')) {
        next({
          path: '/login',
          query: { redirect: to.fullPath }
        })
      } else {
        next()
      }
    },

    children:  [
      { path: '', component: () => import('pages/HomeUser.vue') }
    ]
  },

  {
    path: '/new/project',
    component: () => import('layouts/LoggedLayout.vue'),
    meta: { requiresAuth: true },
    beforeEnter: (to, from, next) => {
      if (isTokenExpired(getRefreshToken(), getTimestampRefreshToken(), '1d')) {
        next({
          path: '/login',
          query: { redirect: to.fullPath }
        })
      } else {
        next()
      }
    },

    children:  [
      { path: '', component: () => import('pages/NewProject.vue') }
    ]
  },

  {
    path: '/home/:uid/project/:pid',
    component: () => import('layouts/LoggedLayout.vue'),
    meta: { requiresAuth: true },
    beforeEnter: (to, from, next) => {
      if (isTokenExpired(getRefreshToken(), getTimestampRefreshToken(), '1d')) {
        next({
          path: '/login',
          query: { redirect: to.fullPath }
        })
      } else {
        next()
      }
    },

    children:  [
      { path: '', component: () => import('pages/ProjectPage.vue'), props: route => ({ key: route.params.pid }) }
    ]
  },

  {
    path: '/new/business',
    component: () => import('layouts/LoggedLayout.vue'),
    meta: { requiresAuth: true },
    beforeEnter: (to, from, next) => {
      if (isTokenExpired(getRefreshToken(), getTimestampRefreshToken(), '1d')) {
        next({
          path: '/login',
          query: { redirect: to.fullPath }
        })
      } else {
        next()
      }
    },

    children:  [
      { path: '', component: () => import('pages/NewBusiness.vue') }
    ]
  },

  {
    path: '/home/:uid/business/:bid',
    component: () => import('layouts/LoggedLayout.vue'),
    meta: { requiresAuth: true },
    beforeEnter: (to, from, next) => {
      if (isTokenExpired(getRefreshToken(), getTimestampRefreshToken(), '1d')) {
        next({
          path: '/login',
          query: { redirect: to.fullPath }
        })
      } else {
        next()
      }
    },

    children:  [
      { path: '', component: () => import('pages/BusinessPage.vue'), props: route => ({ key: route.params.pid }) }
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
