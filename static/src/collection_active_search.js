import $ from "jquery";

import { addToCollection, removeFromCollection, createCollectionRequest } from './requests';

$(function () {
    $(".q-collection").on("changed.bs.select", function(e, clickedIndex, newValue, oldValue) {
      const id = $(this).find('option').eq(clickedIndex).data('id');
      const question_id = $(this).find('option').eq(clickedIndex).data('questionid');
      if (newValue){
        addToCollection(id,question_id)
      }else{
        removeFromCollection(id,question_id)
      }
    });
});

$('.new-collection').click( async function(){
    const name = prompt("Nazwa Kolekcji");
    const collection_id = await createCollectionRequest(name);
    if (! collection_id){
        return
    }
    $('.new-collection').each(function(){
        const questionId = $(this).data('questionid');
        const select = $(this).parent().find('select.q-collection').eq(0);
        select.append(`<option data-id="${collection_id}" data-questionid="${questionId}">${name}</option>`);
        select.selectpicker("refresh")
    })
});

