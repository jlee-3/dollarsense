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
app.mount('#app')
