import $ from "jquery";

$.ajaxSetup({
    beforeSend:function(xhr,settings){
        xhr.setRequestHeader("X-CSRFToken",csrf)
    }
});

const collectionManagementURL = (collection_id,question_id) => `https://${window.location.host}/collection/${collection_id}/question/${question_id}/`;
const createCollectionURL = `https://${window.location.host}/collection/create/`;

export async function addToCollection(collection_id,question_id){
    try{
    const result =await $.post(collectionManagementURL(collection_id,question_id))
    }catch(err){
        alert("Couldn't add to collection");
    }
}

export async function removeFromCollection(collection_id,question_id){
    try{
    const result = await $.ajax({
        url: collectionManagementURL(collection_id,question_id),
        type: 'DELETE'
    });

    }catch(err){
        alert("Couldn't remove from collection");
    }
}

export async function createCollectionRequest(name){
    try{
    const result =await $.post(createCollectionURL,{'name':name});
    return result.collection_id
    }catch(err){
        alert("Couldn't create collection");
        return null
    }
}
