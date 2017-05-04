const assert    = require('chai').assert;
const sayHello  = require('../app').sayHello;
const addNums   = require('../app').addNumbers;
const fizzBuzz  = require('../app').fizzBuzz;


describe('App', function(){
  context('Initially learning unit testing', function(){
    it('app should return hello', function(){
      var result = sayHello();
      assert.equal(result, 'Hello, there Cutie pie! One of us is in deep trouble.');
    })

    it('app should return a string', function(){
      var result = sayHello();
      assert.typeOf(result, 'string');
    })

    it('addNumbers should add two values', function(){
      var result = addNums(5,5);
      assert.equal(result, 10)
    })

    it('addNumbers is greater than 5', function(){
      var result = addNums(2,4)
      assert.isAbove(result, 5)
      assert.equal(result, 6)
    })

    it('addNumbers returns a number', function(){
      var result = addNums(5,5);
      assert.typeOf(result, 'number')
    })
  })

  context('fizzBuzz', function(){
    it('returns Fizz if divisible by 3', function(){
      var result = fizzBuzz(6);
      assert.equal(result, 'Fizz')
      assert.typeOf(result, 'string')
    })

    it('returns Buzz if divisible by 5', function(){
      var result = fizzBuzz(10);
      assert.equal(result, 'Buzz')
      assert.typeOf(result, 'string')
    })

    it('returns Super if divisible by 7', function(){
      var result = fizzBuzz(14);
      assert.equal(result, 'Super')
      assert.typeOf(result, 'string')
    })
  })
});
