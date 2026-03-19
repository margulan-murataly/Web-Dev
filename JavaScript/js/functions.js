/* function info () {
    console.error("Hello");
    console.error("World!");
}

info(); */
/* 
function info (word, num) {

    console.error("Hello");
    
}

info("123", 0); */
/* 
function superArr(arr0, arr1){
    
    const supArr = [];

    const max_length = arr0.length > arr1.length ? arr0.length : arr1.length;

    //const max_length = Math.max(arr0.length, arr1.length);

    for(let i = 0; i < max_length; ++i) {
        if (arr0[i] !== undefined && arr1[i] !== undefined) {
            supArr.push(arr0[i] * arr1[i]);
        }
        else {
            supArr.push(arr0[i] ?? arr1[i]);
        }
    }

    return supArr;
}

const arr1 = [1, 2, 3, 4, 5]
const arr2 = [1, 2, 3, 4, 5, 6, 7, 8]

console.log(superArr(arr1, arr2)); */