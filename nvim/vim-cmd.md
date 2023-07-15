# horizontal move

- `c`, change which mean delete and switch to insert mode
- `D`, from the cursor and delete to the end
- `S`, from the cursor and delete to the end and switch to insert mode
- `ct)`, delete the content till the bracket and switch to insert mode
- `diW  viW yiW`, delete select or yank the whole word(include the dash and hyphen)
- `f`, find the character and use ==;== jump to next ==,== jump to the previous
- `F`, find from the oposite direction

=======================================================================

# vertical move

- `va{Vd`, if your cursor is inside the funtion, this command can delete the whole function

=======================================================================

# window movement

- `C-wj C-wk C-wh C-wl` move to the differetn window

=======================================================================

# replace

- replace the selected content in visual mode
  - selected content in visual mode
  - `:s/<pattern>/<str>`
- replace all in the file `:%s/<pattern>/<str>`
- replace in one line `:s/<patter>/<str>`

=======================================================================

# macro

- know how to record the command but not really familiar with it

=======================================================================

# register

- don't understand the concept

=======================================================================

# multiline edit

- `C-v` to get into the visual block mode
- `Shift-i or Shift-a` to type in something(notice it only change the
  first line)
- `esc` escape then you will see changes in all the selected lines
