<script lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import { useQuery } from '@vue/apollo-composable'
import { expenseQueryGql } from './graphql/queries'
import { ref, computed } from 'vue'

export default {
  setup() {
    const { result, loading } = useQuery(
      expenseQueryGql,
      // variables
      null,
      // options
      () => ({
        fetchPolicy: 'cache-and-network'
      })
    )

    const allExpenses = computed(() => result.value?.allExpenses ?? [])
    console.log('[Home] result: ', allExpenses)

    return {
      loading,
      allExpenses
    }
  }
}
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <!-- <HelloWorld msg="You did it!" /> -->
      <h1 class="text-3xl font-bold underline text-blue-700">Hello world!</h1>
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <p v-if="loading">loading...</p>
        <p
          v-else-if="allExpenses"
          class="text-blue-700"
          v-for="expense of allExpenses"
          :key="expense.title"
        >
          {{ expense }}
        </p>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
