// getName()
// console.log(x)

// var x = 7;
// function getName(){
//     console.log("akhil vijayakumar")
// }


// var x = 20;
// a();
// b();
// console.log(x)
// function a(){
//     var x = 5
//     console.log(x)
// };


// function b(){
//     var x = 10
//     console.log(x)
// };
// 


// var a;
// console.log(a)
// if (a === undefined){
//     console.log("a is undefined")
// }
// else{

//     console.log("a is not undefined")
// }


// function num(){
//     num1()
//     function num1(){
//         console.log(b)
//     }
// }

// var b =10
// num()

// var a =100
// {
//     var a = 10
//     let b = 20
//     const c = 30
//     console.log(a)
//     console.log(b)
//     console.log(c)
// }
// console.log(a)
// console.log(b)
// console.log(c)


// function x(){
//     var z = 7
//     function y(){
//         console.log(z)
//     }
//     return y
// }
// w = x()
// w()

// function x(){
//     for (var i =1;i <= 6; i++){
//         close(i)
//         }
//     function close(i){
//         setTimeout(function(){
//             console.log(i)
//         },i*1000)
//     }
    
    
// }
// x()


// function xy(parms){
//     console.log(parms)
// }
// var c =function b(){

// }
// xy(c)


// setTimeout(function(){
//     console.log("timer")
// },3000)


// function x(y){
//     console.log("x")
//     y()
// }
// x(function y(){
//     console.log("y")
// })



// let add = (a,b) => a+b

// console.log(add(5,6))



// let sum = (...args) =>{
//     return args.reduce((totel, current)=>totel + current)
// }


// console.log(sum(1,2,3,4,5))




// array = ["Akhil", "Roshan", "Sanup", "Vaishak", "Anupama"]

// array.map((name)=>console.log(name))


// const data = [
//     {
//         name:"Ajith",
//         age:30
//     },
//     {
//         name:"Amal",
//         age:25
//     },
//     {
//         name:"Pranav",
//         age:21
//     }
// ]


// data.map((data)=>console.log(`My name is ${data.name} and am ${data.age} years old`))



// list = [1,2,3,4,5]

// function mul(n){
//     return n*n
// }


// mulList = list.map(mul, list)
// console.log(mulList)


// const list = [1,2,3,4,6,7,8]

// const [a,b,...v] = list
// console.log(a)
// console.log(v)



// list = [1,2,3,4,5,67,8]



// const even = list.filter((val)=> val%2 == 0)
// console.log(even)




// const people = [
//     {
//         name:"Akhil",
//         superhero : true
//     },
//     {
//         name:"Roshan",
//         superhero:true
//     },
//     {
//         name:"Vaisakh",
//         superhero:true
//     },
//     {
//         name:"Anupama",
//         superhero:true
//     }
// ]



// const isSuper = people.filter(val =>{
//     return val.superhero == true
// }).map((val)=>val.name)


// console.log(isSuper)



// const value = [
//     {
//         name:"Akhil",
//         salary:2355
//     },
//     {
//         name:"Vaisakh",
//         salary:53433
//     },
//     {
//         name:"Roshan",
//         salary:78934
//     },
//     {
//         name:"Anupama",
//         salary:525235
//     }
// ]


// const totelSalary = value.reduce((totelAmount, item)=>{
//     return totelAmount+item.salary
// },0)

// console.log(totelSalary)