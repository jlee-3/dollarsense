/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        'grey-bubble': '#1B1B1C',
        'grey-pill': '#38363E',
        'grey-pill-darker': '#222225',
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
    },
    dropShadow: {
      'grey-pill': '0 35px 35px rgba(0, 0, 0, 0.25)'
    }
  },
  plugins: []
}
