set nocompatible
filetype off

call plug#begin('~/.vim/bundle')

Plug 'bronson/vim-visual-star-search'
Plug 'flazz/vim-colorschemes'
Plug 'godlygeek/tabular'
Plug 'jlanzarotta/bufexplorer'
Plug 'kien/ctrlp.vim'
Plug 'majutsushi/tagbar'
Plug 'nanotech/jellybeans.vim'
Plug 'rakr/vim-one'
Plug 'rakr/vim-two-firewatch'
Plug 'scrooloose/nerdtree'
Plug 'sheerun/vim-polyglot'
Plug 'sjl/gundo.vim'
Plug 'tpope/vim-fugitive'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'vim-scripts/c.vim'
Plug 'vimwiki/vimwiki'

call plug#end()

syntax enable 
filetype plugin indent on
"nnoremap \ ,
"let mapleader="\<space>"
set autoread
set backspace=indent,eol,start
set ch=4
set clipboard=unnamed
set cursorline
set dir=~/tmp
set encoding=utf-8
set exrc
set ff=unix
set foldenable
set foldmethod=syntax
set formatoptions=tcroqln2
set formatoptions-=t "turn off text wrapping
set formatoptions-=c "turn off comment wrapping
set hidden
set history=500
set hlsearch
set ignorecase
set incsearch
set laststatus=2
set linebreak
set nobackup
"set nowritebackup
set noswapfile
set noequalalways
set noexpandtab
set nofoldenable
set nrformats=
set number
set relativenumber
set path=.,,
set printoptions=number:n,syntax:n,paper:letter
set ruler
set scrolloff=3
set sessionoptions+=blank,buffers,curdir,folds,help,options,tabpages,winsize,unix,resize,localoptions,winpos
set shellpipe=>
set shiftwidth=4
set showcmd
set showmatch
set smartcase
set smartindent
set softtabstop=4
set expandtab
set tabstop=4
set tags=tags;~/;./tags
set splitbelow
set splitright
set termguicolors
set textwidth=120
set visualbell
set wildmenu
"set wildmode=list:longest,full
set wildmode=full
set wrap
set wrapscan

"====================================================================================
if has("autocmd")
    autocmd BufEnter :filetype detect
    "autocmd FileType * nested :call tagbar#autoopen(0)

    augroup c
        autocmd!
        autocmd FileType c map <F9> :!cl %<CR>
    augroup END

    augroup javascript
        autocmd!
        autocmd FileType javascript map <F9> :w!<CR> :!"/usr/bin/nodejs" %<CR>
    augroup END

    augroup python
        autocmd!
        autocmd FileType python setlocal omnifunc=pythoncomplete#Complete
        autocmd FileType python setlocal expandtab
        autocmd FileType python setlocal foldmethod=indent
        autocmd FileType python setlocal foldlevel=99 
        autocmd FileType python map <F9> :!python %
        autocmd FileType python lcd %:p:h
        "autocmd FileType python nested :call tagbar#autoopen(0)
    augroup END

    augroup java
        autocmd!
        autocmd FileType java setlocal omnifunc=javacomplete#Complete
        autocmd FileType java setlocal makeprg=ant\ -f\ build/build.xml\ tomcat.deploy
        autocmd FileType java setlocal efm=%A\ %#[javac]\ %f:%l:\ %m,%-Z\ %#[javac]\ %p^,%-C%.%#
        "autocmd FileType java nested :call tagbar#autoopen(0)
    augroup END

    autocmd BufRead,BufNewFile *.ddl setfiletype sql
    autocmd FileReadPost <buffer> *.txt set noai

    augroup web
        autocmd!
        autocmd FileType jsp set foldmethod=marker foldmarker=%>,<%
    augroup END
endif
"====================================================================================

if has("win16") || has("win32") || has("win64")
    let s:os = "win"
    au GUIEnter * simalt ~x
else
    let s:os = substitute(system('uname'), "\n", "", "")
    set columns=256
    set lines=158
endif

"====================================================================================

if has("gui")
    let g:mimic_font_style=3
    "set background=dark
    
    "color abra
    "color advantage
    "color apprentice
    "color aqua
    "color breezy
    "color candy
    "color chlordane
    "color codeschool
    "color darkspectrum
    "color darkZ
    "color github
    "color gruvbox
    "color intellij
    color jellybeans
    "color lucius
    "color molokai
    "color moria
    "color one
    "color pyte
    "color railscasts
    "color Spink
    "color summerfruit
    "color summerfruit256
    "color synic
    "color twilight
    "color wombat
    "color wombat256
    "color xoria256
    "color zenburn
    "color darcula
    "color badwolf

    if s:os == "win"
        "set guifont=Courier_New:h8:cANSI
        "set guifont=Courier:h9:cANSI:qDRAFT
        "set guifont=Lucida_Console:h8:cANSI
        set guifont=Consolas:h8:cANSI:qDRAFT
        "set guifont=Anonymous:h8:cANSI
    else
        "set guifont=Courier\ 10\ Pitch\ 9 
        set guifont=Inconsolata\ Medium\ 12 
        "set guifont=Consolas\ 10 
        "set guifont=Andale\ Mono\ 10
    endif

    set guioptions-=T
    set guioptions-=r
    set guioptions-=l
    set guioptions-=m
else
    set lines=43
    set columns=166
    color ibmedit
    "color 0x7A69_dark
    color wombat
endif

let treeExplVertical=1
let treeExplHidden=1

nnoremap <leader>c                  :set cursorline!<CR>
nnoremap <leader>du                 :!dos2unix %<CR>
imap <C-h>                          <Left>
imap <C-j>                          <Down>
imap <C-k>                          <Up>
imap <C-l>                          <Right>
nmap <A-Up>                         :.m.-2<CR>
nmap <A-Down>                       :.m.+1<CR>
imap <C-s>                          <Esc>:up<CR>a
imap <C-d>                          <C-o>dd
inoremap <C-F5>                     <C-R>=strftime("%c")<CR>
inoremap <Nul>                      <C-x><C-o>
map <A-m>                           :message<CR>
map <A-r>                           {gq}
map <C-\>                           :tselect<CR>
map <C-F10>                         :%s/<\/\?\zs\(\a\+\)\ze[ >]/\L\1/g<CR>
map <C-F9>                          :%s/\(<[^>]*\)\@<=\<\(\a*\)\ze=['"]/\L\2/g<CR>
map <C-Left>                        zM
map <C-Right>                       zR
map <C-s>                           :up<CR>
map <Down>                          <Nop>
map <Right>                         <Nop>
map <Left>                          <Nop>
map <Up>                            <Nop>
map <F11>                           :edit $MYVIMRC<CR>
map <F3>                            :NERDTreeToggle<CR>
map <F2>                            :vs.<CR>    
map <A-F3>                          :Vexplore<CR>
map <F4>                            :TagbarToggle<CR>
map <F5>                            :vimgrep /
map <M-F5>                          :vimgrep /<C-R><C-W>/
map <M-l>                           :g/<C-R><C-W>/<CR> 
map <silent> <leader>g              g]
map <silent> <leader>m              :verb map<CR>
nmap <silent> <leader>n             :silent :nohlsearch<CR>
nmap <silent> <leader>o             :silent :only<cr>
nnoremap '                          `
nnoremap `                          '
nnoremap <C-F5>                     "=strftime("%c")<CR>P
nnoremap <C-h>                      <C-w>h
nnoremap <C-j>                      <C-w>j
nnoremap <C-k>                      <C-w>k
nnoremap <C-l>                      <C-w>l
nnoremap <F6>                       :GundoToggle<CR>
nnoremap <silent> [B                :bfirst<CR> 
nnoremap <silent> [b                :bprevious<CR> 
nnoremap <silent> [C                :cfirst<CR> 
nnoremap <silent> [c                :cprevious<CR> 
nnoremap <silent> [L                :lfirst<CR> 
nnoremap <silent> [l                :lprevious<CR> 
nnoremap <silent> [T                :tfirst<CR> 
nnoremap <silent> [t                :tprevious<CR> 
nnoremap <silent> ]B                :blast<CR> 
nnoremap <silent> ]b                :bnext<CR> 
nnoremap <silent> ]C                :clast<CR> 
nnoremap <silent> ]c                :cnext<CR> 
nnoremap <silent> ]L                :llast<CR> 
nnoremap <silent> ]l                :lnext<CR> 
nnoremap <silent> ]T                :tlast<CR> 
nnoremap <silent> ]t                :tnext<CR> 
"nnoremap j                             gj
"nnoremap k                             gk
"nnoremap gk                            k
"nnoremap gj                            j
vmap <A-Down>                       xp`[V`]
vmap <A-Up>                         xkP`[V`]

nnoremap <C-F1> :if &go=~#'m'<Bar>set go-=m<Bar>else<Bar>set go+=m<Bar>endif<CR>
nnoremap <C-F2> :if &go=~#'T'<Bar>set go-=T<Bar>else<Bar>set go+=T<Bar>endif<CR>
nnoremap <C-F3> :if &go=~#'r'<Bar>set go-=r<Bar>else<Bar>set go+=r<Bar>endif<CR>

nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l

xnoremap * :<C-u> call <SID>VSetSearch()<CR>/<C-R>=@/<CR><CR>
xnoremap # :<C-u> call <SID>VSetSearch()<CR>?<C-R>=@/<CR><CR>

" backspace in Visual mode deletes selection
vnoremap <BS> d

" CTRL-X and SHIFT-Del are Cut
vnoremap <C-X> "+x
vnoremap <S-Del> "+x

" CTRL-C and CTRL-Insert are Copy
vnoremap <C-C> "+y
vnoremap <C-Insert> "+y

" CTRL-V and SHIFT-Insert are Paste
map <C-V>           "+gP
map <S-Insert>      "+gP

cmap <C-V>      <C-R>+
cmap <S-Insert>     <C-R>+

"NERDTree options
let g:NERDTreeIgnore=['\.$', '\.\.$', '\.svn$', '\.class$', '\.jar$', '\.pdf$', '\.png$', '\.gif$', '\.settings$']
let g:NERDChristmasTree=1
let g:NERDTreeShowBookmarks=1
"let NERDTreeShowHidden=1
let g:NERDTreeChDirMode=2
"let NERDTreeWinSize=45
"let NERDTreeDirArrows=0

let g:ragtag_global_maps=1 

let g:FoldMethod=1

function! ShowJSP()
    set foldmethod=marker
    set foldmarker=%>,<%
    let g:FoldMethod = 1
endfunction

function! ShowHTML()
    set foldmethod=marker
    set foldmarker=<%,%>
    let g:FoldMethod = 0
endfunction

function! ToggleFold() 
    if g:FoldMethod == 1
        exe 'call ShowHTML()'
    else
        exe 'call ShowJSP()'
    endif
endfunction

function! s:VSetSearch()
    let temp = @s
    norm! gv"sy
    let @/ = '\V' . substitute(escape(@s, '/\'), '\n', '\\n', 'g')
    let @s = temp
endfunction

map <A-Right>           :bn<CR>
map <A-Left>            :bp<CR>

let g:tagbar_left=0

let g:ctrlp_working_path_mode = 0
let g:ctrlp_extensions=['tag', 'quickfix', 'dir']
let g:ctrlp_clear_cache_on_exit = 1
let g:ctrlp_custom_ignore = { 
    \ 'dir': '\.svn$\|\.git$\|target$\|warFiles$', 
    \ 'file': '\.class$\|\.jar$', 
    \ 'link': '' 
    \ }
let g:tagbar_ctags_bin='/usr/bin/ctags'
let g:EclimJavascriptValidate=0

nnoremap <silent> <buffer> <leader>i :JavaImport<cr>
nnoremap <silent> <buffer> <cr> :JavaSearchContext

" Define a command to make it easier to use
command! -nargs=+ QFDo call QFDo(<q-args>)

" Function that does the work
function! QFDo(command)
    " Create a dictionary so that we can
    " get the list of buffers rather than the
    " list of lines in buffers (easy way
    " to get unique entries)
    let buffer_numbers = {}
    " For each entry, use the buffer number as 
    " a dictionary key (won't get repeats)
    for fixlist_entry in getqflist()
        let buffer_numbers[fixlist_entry['bufnr']] = 1
    endfor
    " Make it into a list as it seems cleaner
    let buffer_number_list = keys(buffer_numbers)

    " For each buffer
    for num in buffer_number_list
        " Select the buffer
        exe 'buffer' num
        " Run the command that's passed as an argument
        exe a:command
        " Save if necessary
        update
    endfor
endfunction

let wiki_1 = {}
let wiki_1.path = '~/Dropbox/exocortex/vimwiki'
let wiki_1.path_html = '~/Dropbox/exocortex/vimwiki/html'
let wiki_1.auto_toc = 1

let g:vimwiki_list = [wiki_1]
let g:one_allow_italics=1
let g:airline_theme='one'

