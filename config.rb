wiki_options = {
  allow_editing: false,
  critic_markup: true,
  display_metadata: false,
  emoji: true,
  index_page: 'home',
  page_file_dir: 'pages',
  sidebar: :left,
}

# Load wiki options into the proper space
Precious::App.set(:wiki_options, wiki_options)
