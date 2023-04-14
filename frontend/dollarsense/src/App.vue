<script lang="ts">
import { RouterLink, RouterView, useRoute } from 'vue-router'
import { computed } from 'vue'
import DashboardIcon from './components/icons/IconDashboardMain.vue'
import ExpenseIcon from './components/icons/IconExpenseMain.vue'
// import HelloWorld from './components/HelloWorld.vue'

export default {
  setup() {
    const menuItems = ['Dashboard', 'Expenses']
    const route = useRoute()
    const path = computed(() => route.path)

    return {
      menuItems,
      path
    }
  },
  components: {
    // HelloWorld
    DashboardIcon,
    ExpenseIcon
  }
}
</script>

<template>
  <div class="flex flex-row h-screen w-screen">
    <!-- sidebar -->
    <header class="bg-grey-bubble w-96 pt-14">
      <!-- <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" /> -->

      <div class="wrapper mx-auto w-fit">
        <!-- <HelloWorld msg="You did it!" /> -->
        <h1 class="font-logo text-4xl font-bold text-white">Dollarsense</h1>
        <br />
        <nav class="flex-col">
          <RouterLink
            :to="`${menuItem.toLowerCase()}`"
            class="font-inter font-semibold px-4 mb-2 -ml-4 h-10 w-fit rounded-xl text-lg flex items-center hover:bg-theme-green-hover"
            :class="path.slice(1) === menuItem.toLowerCase() ? 'text-theme-green' : 'text-white'"
            v-for="menuItem of menuItems"
          >
            <DashboardIcon v-if="menuItem.toLowerCase() === 'dashboard'" class="mr-2" />
            <ExpenseIcon v-else-if="menuItem.toLowerCase() === 'expenses'" class="mr-2" />
            {{ menuItem }}
          </RouterLink>
        </nav>
      </div>
    </header>

    <!-- page -->
    <RouterView />
  </div>
</template>

<!-- <style scoped>
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
</style> -->
