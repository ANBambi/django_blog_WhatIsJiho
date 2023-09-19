tinymce.init({
    selector: '#content',
    plugins: 'fullscreen',
    toolbar: 'fullscreen',
    width: 1000,
    height: 500,
    plugins:[
        'advlist', 'autolink', 'link', 'image', 'lists', 'charmap', 'prewiew', 'anchor', 'pagebreak',
        'searchreplace', 'wordcount', 'visualblocks', 'code', 'fullscreen', 'insertdatetime', 'media', 
        'table', 'emoticons', 'template', 'codesample'
    ],
    toolbar: 'undo redo | styles | bold italic underline | alignleft aligncenter alignright alignjustify |' + 
    'bullist numlist outdent indent | link image | print preview media fullscreen | ' +
    'forecolor backcolor emoticons',
    menu: {
        favs: {title: 'menu', items: 'code visualaid | searchreplace | emoticons'}
    },
    menubar: 'favs file edit view insert format tools table',
    content_style: 'body{font-family:Helvetica,Arial,sans-serif; font-size:16px}'
});

const modalOpenBtn = document.getElementById('modal-open-btn')
const modalCloseBtn = document.getElementById('modal-close-btn')
const modalWrapper = document.getElementsByClassName("modal-wrapper")[0]

modalOpenBtn.addEventListener("click", ()=>{
    modalWrapper.style.display = "flex";
})

modalCloseBtn.addEventListener("click", ()=>{
    modalWrapper.style.display = "none";
})



const writeTitle = document.getElementById('title')
const writeContent = document.getElementById('content')
const modifyButton = document.getElementsByClassName('modify_button')[0]

function modifyClikc() {
    
}

