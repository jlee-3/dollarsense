/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        'grey-bubble': '#1B1B1C',
        'grey-pill': '#38363E',
        'dark-background': '#131416',
        'theme-green': '#03C988',
        'theme-green-hover': 'rgba(3, 201, 136, 0.2)',
        'theme-green-highlight': '#00ECD0',
        'soft-white': '#D6D6D6',
        'soft-gray': '#989898'
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
