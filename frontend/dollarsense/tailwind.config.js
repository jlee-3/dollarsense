/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        'grey-bubble': '#1B1B1C',
        'grey-pill': '#38363E',
        'grey-pill-highlight': '#4D4B55',
        'grey-pill-darker': '#222225',
        'dark-background': '#131416',
        'theme-green': '#03C988',
        'theme-green-hover': 'rgba(3, 201, 136, 0.2)',
        'theme-green-highlight': '#00ECD0',
        'theme-orange': '#E1522B',
        'soft-white': '#D6D6D6',
        'soft-gray': '#989898'
      }
    },
    fontFamily: {
      logo: ['"Saira Condensed"'],
      main: ['Inter'],
      numeric: ['"Roboto Mono"']
    },
    dropShadow: {
      'grey-pill': '0 35px 60px -15px rgba(0, 0, 0, 0.3)'
    }
  },
  plugins: []
}
