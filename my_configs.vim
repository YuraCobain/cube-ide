set number
set gfn=IBM\ Plex\ Mono\ 10

" YCM mapping
nnoremap <leader>yl :YcmCompleter GoToDeclaration<CR>
nnoremap <leader>yf :YcmCompleter GoToDefinition<CR>
nnoremap <leader>yy :YcmCompleter GoToDefinitionElseDeclaration<CR>
nnoremap <leader>ys :YcmCompleter GoToReferences<CR>
nnoremap <leader>yr :<c-u>YcmCompleter RefactorRename <C-R>=Abolish.Coercions.s(expand("<cword>"))<CR>

" Close preview window after completing the insertion
let g:ycm_autoclose_preview_window_after_insertion = 1
let g:ycm_autoclose_preview_window_after_completion = 1

let g:ycm_confirm_extra_conf = 0                " Don't confirm python conf
let g:ycm_always_populate_location_list = 1     " Always populae diagnostics list
let g:ycm_enable_diagnostic_signs = 1           " Enable line highligting diagnostics
let g:ycm_open_loclist_on_ycm_diags = 1         " Open location list to view diagnostics

let g:ycm_max_num_candidates = 20               " Max number of completion suggestions 
let g:ycm_max_num_identifier_candidates = 10    " Max number of identifier-based suggestions
let g:ycm_auto_trigger = 1                      " Enable completion menu
let g:ycm_show_diagnostic_ui = 1                " Show diagnostic display features
let g:ycm_error_symbol = '>>'                   " The error symbol in Vim gutter
let g:ycm_enable_diagnostic_signs = 1           " Display icons in Vim's gutter, error, warnings
let g:ycm_enable_diagnostic_highlighting = 1    " Highlight regions of diagnostic text
let g:ycm_echo_current_diagnostic = 1           " Echo line's diagnostic that cursor is on
let g:ycm_clangd_args=['--header-insertion=never']

set completeopt-=preview

"vimspector mapping
let g:vimspector_enable_mappings = 'HUMAN'
nnoremap <leader>dd :call vimspector#Launch() <CR>

let g:clang_format#style_options = {
            \ "AccessModifierOffset" : -4,
            \ "AllowShortIfStatementsOnASingleLine" : "true",
            \ "AlwaysBreakTemplateDeclarations" : "true",
            \ "SortIncludes" : "false",
            \ "ColumnLimit" : 100,
            \ "Standard" : "C++11"}

" map to <Leader>cf in C++ code
autocmd FileType c,cpp,objc nnoremap <buffer><Leader>cf :<C-u>ClangFormat<CR>
autocmd FileType c,cpp,objc vnoremap <buffer><Leader>cf :ClangFormat<CR>
" if you install vim-operator-user
autocmd FileType c,cpp,objc map <buffer><Leader>x <Plug>(operator-clang-format)
" Toggle auto formatting:
nmap <Leader>C :ClangFormatAutoToggle<CR>
autocmd FileType c ClangFormatAutoEnable

autocmd VimEnter * NERDTree

"GTest
augroup GTest
	autocmd FileType cpp nnoremap <silent> <leader>tt :GTestRun<CR>
	autocmd FileType cpp nnoremap <silent> <leader>tu :GTestRunUnderCursor<CR>
	autocmd FileType cpp nnoremap          <leader>tc :GTestCase<space>
	autocmd FileType cpp nnoremap          <leader>tn :GTestName<space>
	autocmd FileType cpp nnoremap <silent> <leader>te :GTestToggleEnabled<CR>
	autocmd FileType cpp nnoremap <silent> ]T         :GTestNext<CR>
	autocmd FileType cpp nnoremap <silent> [T         :GTestPrev<CR>
	autocmd FileType cpp nnoremap <silent> <leader>tf :CtrlPGTest<CR>
	autocmd FileType cpp nnoremap <silent> <leader>tj :GTestJump<CR>
	autocmd FileType cpp nnoremap          <leader>ti :GTestNewTest<CR>i
augroup END
