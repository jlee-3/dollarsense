import { createApp, h, provide } from 'vue'
import App from './App.vue'
import router from './router'
import { ApolloClient, ApolloLink, InMemoryCache, createHttpLink } from '@apollo/client/core'
import { ApolloClients } from '@vue/apollo-composable'
import './index.css'
import './assets/main.css'

// HTTP connection to the API
const httpLink = createHttpLink({
  uri: 'http://127.0.0.1:8000/graphql/' // Matches the url and port that Django is using
})

const apolloClient = new ApolloClient({
  link: httpLink, // Matches the url and port that Django is using
  cache: new InMemoryCache()
})

const app = createApp({
  setup() {
    provide(ApolloClients, {
      default: apolloClient
    })
  },
  render: () => h(App)
})

app.use(router)

const clickOutside = {
  beforeMount: (el: any, binding: any) => {
    el.clickOutsideEvent = (event: any) => {
      // check that click occurs outside the el and its children
      // and if it did, call method provided in attribute value
      if (!(el == event.target || el.contains(event.target))) {
        binding.value()
      }
    }
    document.addEventListener('click', el.clickOutsideEvent)
  },
  unmounted: (el: any) => {
    document.removeEventListener('click', el.clickOutsideEvent)
  }
}
app.directive('clickOutside', clickOutside)

app.mount('#app')
