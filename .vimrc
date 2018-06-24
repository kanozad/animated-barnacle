set nocompatible
filetype off

packadd minpac
call minpac#init()

call minpac#add('bronson/vim-visual-star-search')
call minpac#add('flazz/vim-colorschemes')
call minpac#add('godlygeek/tabular')
call minpac#add('jlanzarotta/bufexplorer')
call minpac#add('junegunn/fzf')
call minpac#add('junegunn/fzf.vim')
call minpac#add('kien/ctrlp.vim')
call minpac#add('majutsushi/tagbar')
call minpac#add('nanotech/jellybeans.vim')
call minpac#add('rakr/vim-one')
call minpac#add('rakr/vim-two-firewatch')
call minpac#add('scrooloose/nerdtree')
call minpac#add('sheerun/vim-polyglot')
call minpac#add('sjl/gundo.vim')
call minpac#add('tpope/vim-fugitive')
call minpac#add('tpope/vim-projectionist')
call minpac#add('tpope/vim-scriptease')
call minpac#add('tpope/vim-unimpaired')
call minpac#add('tpope/vim-vinegar')
call minpac#add('vim-airline/vim-airline')
call minpac#add('vim-airline/vim-airline-themes')
call minpac#add('vim-scripts/c.vim')
call minpac#add('vimwiki/vimwiki')

command! PackUpdate call minpac#update()
command! PackClean call minpac#clean()

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
set textwidth=120
set visualbell
set wildmenu
"set wildmode=list:longest,full
set wildmode=full
set wrap
set wrapscan
set lines=43
set columns=132

"====================================================================================

"====================================================================================

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

"set guifont=Courier_New:h8:cANSI
"set guifont=Courier:h9:cANSI:qDRAFT
"set guifont=Lucida_Console:h8:cANSI
set guifont=Consolas:h8:cANSI:qDRAFT
"set guifont=Anonymous:h8:cANSI
"set guifont=Courier\ 10\ Pitch\ 9 
set guifont=Inconsolata\ Medium\ 12 
"set guifont=Consolas\ 10 
"set guifont=Andale\ Mono\ 10

set guioptions-=T
set guioptions-=r
set guioptions-=l
set guioptions-=m

let treeExplVertical=1
let treeExplHidden=1

nnoremap <leader>c                  :set cursorline!<CR>
nnoremap <leader>du                 :!dos2unix %<CR>
nnoremap <A-p>                      :<C-u>FZF<CR>
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
"map <F3>                            :Explore.<CR>
map <leader>e                       :e ~/Dropbox/exocortex<CR>
map <C-F3>                          :e %:h<CR>
map <A-F3>                          :E /home/kanozad/dev/workspaces<CR>
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
"let g:NERDTreeIgnore=['\.$', '\.\.$', '\.svn$', '\.class$', '\.jar$', '\.pdf$', '\.png$', '\.gif$', '\.settings$']
"let g:NERDChristmasTree=1
"let g:NERDTreeShowBookmarks=1
"let NERDTreeShowHidden=1
"let g:NERDTreeChDirMode=2
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
