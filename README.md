# vimLaTeXsnippets
Custom LaTeX snippets for UltiSnips. These snippets are in addition to the standard ones provided by [honza/vim-snippets.]( https://github.com/honza/vim-snippets) Includes single character snippets for all greek letters and abbreviations for various mathematical statements. 

To use include the line
```
extends texgreek, texstatements
```
in the `tex.snippets` file.

The `math()` context is due to [Gilles Castel](https://castel.dev/), read his very nice [blog post](https://castel.dev/post/lecture-notes-1/) about livetyping LaTeX notes in vim.
