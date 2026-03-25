export default {
  content: [
    './.vitepress/**/*.{js,ts,vue}',
    './**/*.md'
  ],
  theme: {
    extend: {
      maxWidth: {
        'content': '768px'
      },
      colors: {
        primary: '#000',
        secondary: '#666'
      }
    }
  }
}