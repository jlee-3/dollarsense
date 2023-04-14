/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        'grey-bubble': '#1B1B1C',
        'dark-background': '#131416',
        'theme-green': '#03C988'
      }
    },
    fontFamily: {
      logo: ['"Saira Condensed"'],
      main: ['Inter'],
      numeric: ['"Roboto Mono"']
    }
  },
  plugins: []
}
