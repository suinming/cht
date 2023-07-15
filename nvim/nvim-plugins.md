# vim.fugitive

- `:G ac` git add all and go to the commit template
- `:G co <branch name>` git checkout branch
- `<leader>G` 3 split window merge
  1.  stay in the middle workspace
  2.  `<leader>rj` //2 is the target branch(_i.e. master branch_)
  3.  `<leader>rk` //3 is the merge branch(_i.e. feature branch_)
  4.  `:only` to see the result

=======================================================================

# vim.emmet([tutorial](https://raw.githubusercontent.com/mattn/emmet-vim/master/TUTORIAL))

- expand abbrev => abbrev + c-y,
- wrap abbrev => visual select + c-y, => Tag: ul>li
- go to next and previous edit point => c-y + n , c-y + N
- remove tag => c-y + k
- split/join tag => c-y + j
- toggle comment => c-y + /

=======================================================================

# vim.bookmarks

- `mi` add the annotation to the book mark
- `mm` add/remove the book mark
- `ma` show all the book mark
- `mc` clear the book marks in current buffer
- `mx` clear all the book marks in current buffer
- `mp` to previous book mark
- `mn` to next book mark

=======================================================================

# nvim-surround

- [doc](https://github.com/kylechui/nvim-surround/blob/main/doc/nvim-surround.txt)
- `ysiw<replace surround>` add the surrounding to the word
- `yss<replace surround>` add the surrounding to the whole line
- `cs<original surround><replace surround>` change the original surrounding to the new surrounding
- `ds<original surround>` delete the surround

=======================================================================

# harpoon

- `<leader>a` => add to harpoon
- `<C-e>` => toggle the harpoon menu
- `<leader>s, d, f, j, k, l` => nav files

=======================================================================

# flash(it might be the solution for the vertical movement)

- `s` => search the target from the beginning of the word(it will
  display the tag for navigation, so basically you can navigate to any
  place in 2 key strokes)
- `S`
  - tree sitter, which can help you select the block of content more efficently
  - after getting into tree sitter you can use ; and , to increase/decrease the selection

=======================================================================

# image-preview

- `<leader>p` in the neo-tree and oil.nvim you can preview the image, and press enter
  to close the preview window

=======================================================================

# telescope-media-files

- `<leader>fp` to open the media preview in telescope but you can not
  see the preview picture(it will show chafa :animate is not found,
  not sure the option in chafa, maybe it will be fixed one day)

=======================================================================

#

=======================================================================

#

=======================================================================

#

=======================================================================

#

=======================================================================

#

=======================================================================
