# change local and remote branch name

```shell
# Rename the local branch to the new name
git branch -m <old_name> <new_name>

# delete remote branch
git push <remote> :<old_name>

# Prevent git from using the old name when pushing in the next step. Otherwise, git will use the old upstream name instead of <new_name>.
git branch --unset-upstream <new_name>

# Push the new branch to remote
git push <remote> <new_name>

# Reset the upstream branch for the new_name local branch
git push <remote> -u <new_name>
```

=======================================================================

# git ignore not working

gitignore 的檔案若已經 commit 的話，gitignore 並不會生效，目前 git 也沒有 automatic 去清除，必須手動清除 cache

- 刪除在.gitgnore 中的檔案 `git rm -r --cached .`
- 新增索引刪除的檔案到 commit 區 `git add --all`
- 新增 commit`git commit -m "fixed untracked files"`
- # push 到遠端`git push origin <branch-name>`

=======================================================================

# git change commit message

there are three conditions :

## condition-1 change the most recent commit(without push to remote

repo)

`git commit --amend`

## condition-2 change the most recent commit message(after push to remote)

- 用amend flag修改最新的commit message`git commit --amend`
- force push 到remote repo `git push --force <remoteName> <branchName>`
  ex: `git push --force origin master`

## condition-3 change older or multiple commits(strongly discouraged)

- `git rebase -i HEAD~N`用rebase的interactive mode修改最新的N個commits

輸完指令將會開啟新視窗：

```shell
pick 43f8707f9 fix: update dependency json5 to ^2.1.1
pick cea1fb88a fix: update dependency verdaccio to ^4.3.3
pick aa540c364 fix: update dependency webpack-dev-server to ^3.8.2
pick c5e078656 chore: update dependency flow-bin to ^0.109.0
pick 11ce0ab34 fix: Fix spelling.

# Rebase 7e59e8ead..11ce0ab34 onto 7e59e8ead (5 commands)
```

- 在想修改的commit前面，將pick改成reword

```shell
reword 43f8707f9 fix: update dependency json5 to ^2.1.1
reword cea1fb88a fix: update dependency verdaccio to ^4.3.3
pick aa540c364 fix: update dependency webpack-dev-server to ^3.8.2
pick c5e078656 chore: update dependency flow-bin to ^0.109.0
pick 11ce0ab34 fix: Fix spelling.

# Rebase 7e59e8ead..11ce0ab34 onto 7e59e8ead (5 commands)
```

- 保存並離開編輯器
- 用上述例子為例，想修改的commit有兩個，因此接下來開啟兩次編輯器讓你修改commit
  message

- `git push --force <remoteName> <branchName>`
  強置將修改的commit推到遠端

=======================================================================

# 回覆索引區的檔案狀態

## condition-1 將加到索引區的文件回覆到modified的狀態，並復原修改前的工作區

- `git restore <filename>` 將工作區(還沒add)的文件復原到修改前的狀態
- `git restore --staged <filename>` 將索引區(已經add)的文件復原到上一次commit的SHA1值

## condition-2 將文件從索引區中刪除，使得文件變成untracked的狀態

- # `git rm --cached <filename>` 直接將索引區所紀錄的文件刪除，使得文件的狀態變成untracked

=======================================================================

# git tags 使用備忘錄

- tagging is generally used to capture a point in history that is used for a ==marked version release==
- create tag 
  1.  `git tag <tag name>` create a lightweight tag
  2.  `git tag -a <tag name> <commit SHA1> -m <some tag message>` create a annotated tag(it will also create a blob in .git/objects)
- list tags `git tag`
- delete tag
  1.  `git tag -d <tag name>` delete a local tag
  2.  `git push --delete origin <tag name>` delete a remote tag
- push tag
  1.  `git push origin <tag name>` push a local tag to remote
  2.  `git push --tags` push multiple tag
- tag naming best practice
  - A.B.C
    - A大的feature更新
    - B小的feature更新
    - C修復bug

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

#

=======================================================================
