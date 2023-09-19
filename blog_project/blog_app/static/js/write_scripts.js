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
const modalSaveBtn = document.getElementById('modal-save-button')
const modalWrapper = document.getElementsByClassName("modal-wrapper")[0]
const toxEditor = document.getElementsByClassName("write-box")[0]
const postInfoBox = document.getElementsByClassName("post-info-box")[0]


modalOpenBtn.addEventListener("click", ()=>{
    modalWrapper.style.display = "flex";
    toxEditor.style.display = 'none';
    postInfoBox.style.display = 'none';
})

modalCloseBtn.addEventListener("click", ()=>{
    modalWrapper.style.display = "none";
    toxEditor.style.display = 'flex';
    postInfoBox.style.display = 'flex';

})

modalSaveBtn.addEventListener("click", ()=>{
    toxEditor.style.display = 'flex';
    postInfoBox.style.display = 'flex';
})