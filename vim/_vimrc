set nocompatible
filetype off

call plug#begin('~/vimfiles/bundle')

Plug 'blueshirts/darcula'
Plug 'bronson/vim-visual-star-search'
Plug 'flazz/vim-colorschemes'
Plug 'godlygeek/tabular'
Plug 'jlanzarotta/bufexplorer'
Plug 'junegunn/fzf'
Plug 'junegunn/fzf.vim'
Plug 'kien/ctrlp.vim'
Plug 'majutsushi/tagbar'
Plug 'nanotech/jellybeans.vim'
Plug 'rakr/vim-one'
Plug 'rakr/vim-two-firewatch'
Plug 'scrooloose/nerdtree'
Plug 'sgur/vim-editorconfig'
Plug 'sheerun/vim-polyglot'
Plug 'sjl/gundo.vim'
Plug 'tpope/vim-fugitive'
Plug 'tpope/vim-projectionist'
Plug 'tpope/vim-scriptease'
Plug 'tpope/vim-unimpaired'
Plug 'tpope/vim-vinegar'
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
set cmdheight=4
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
let g:mimic_font_style=3
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
"color moria
"color one
"color pyte
"color railscasts
"color spink
"color summerfruit
"color summerfruit256
"color synic
"color twilight
"color wombat
"color wombat256
"color wtf
"color xoria256
"color zenburn
"set background=dark
"color darcula
"color badwolf
"color two-firewatch

"set guifont=Courier_New:h8:cANSI
"set guifont=Courier:h9:cANSI:qDRAFT
"set guifont=Lucida_Console:h8:cANSI
set guifont=Consolas:h9:cANSI:qDRAFT
"set guifont=Menlo:h8:cANSI:qDRAFT
"set guifont=Anonymous:h8:cANSI
au GUIEnter * simalt ~x

set guioptions-=T
set guioptions-=r
set guioptions-=l
set guioptions-=m
"====================================================================================

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
"map <A-F3>                          :E. <CR>
"map <C-F3>                          :e %:h <CR>
"map <F3>                            :Explore C:\dev\workspaces<CR>
map <F3>                            :NERDTreeToggle<CR>
map <C-F3>                          :NERDTree %:h<CR>
map <A-F3>                          :NERDTree c:\dev\workspaces<CR>
map <F2>                            :vs.<CR>    
map <F4>                            :TagbarToggle<CR>
map <F5>                            :vimgrep /
map <M-F5>                          :vimgrep /<C-R><C-W>/
map <M-l>                           :g/<C-R><C-W>/<CR> 
map <leader>e                       :NERDTree c:\users\kanozad\Dropbox\exocortex<CR> 
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
nnoremap j                             gj
nnoremap k                             gk
nnoremap gk                            k
nnoremap gj                            j
vmap <A-Down>                       xp`[V`]
vmap <A-Up>                         xkP`[V`]

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

let g:ragtag_global_maps=1 

let g:FoldMethod=1

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
let g:tagbar_ctags_bin='C:/dev/ctags58/ctags.exe'

let wiki_1 = {}
let wiki_1.path = 'C:\Users\kanozad\Dropbox\exocortex\vimwiki'
let wiki_1.path_html = 'C:\Users\kanozad\Dropbox\exocortex\vimwiki\html'
let wiki_1.auto_toc = 1

let g:vimwiki_list = [wiki_1]

let g:one_allow_italics=1
let g:netrw_banner=0
let g:netrw_liststyle=3
let g:netrw_browse_split=0
let g:netrw_altv=1
let g:netrw_winsize=25

"NERDTree Settings
let NERDTreeShowBookmarks=1
let g:NERDTreeIgnore=['\.$', '\.\.$', '\.svn$', '\.class$', '\.jar$', '\.pdf$', '\.png$', '\.gif$', '\.settings$']
let g:NERDChristmasTree=1
let g:NERDTreeBookmarksSort=1
"let NERDTreeShowHidden=1
let g:NERDTreeChDirMode=2
"let NERDTreeWinSize=45
"let g:NERDTreeDirArrows=0
"let g:NERDTreeDirArrowExpandable='+'
"let g:NERDTreeDirArrowCollapsible='~'
"let g:NERDTreeCascadeSingleChildDir=0
"let g:NERDTreeCascadeOpenSingleChildDir=1
