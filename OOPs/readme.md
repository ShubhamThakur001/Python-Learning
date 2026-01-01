Procedural/functional approach is not a lot helpful for real world use cases.

procedural > line by line
functional > code reuse

it is always helpful if we could create a blueprint of what we want and then create multiple copy via it.

so, oops help us in doing below things.
    > define our own datatype
    > generality to specificity

oops is a programming paradidm which help us to write better code

oops
    class
    objects
    encapsulations
    inheritance
    polymorphism
    abstraction


class 
    blueprint , self defined datatyped
    all data types are build in class in python

    > class
        data/attributes/property
        behaviour/method

object

    an object is an instance of our class
    everything in python is an object


constructor and self 

    __init__

    whenever we create/construct an object of a class , there is an inbuild method (__init__) which is called knows as constructor.

    advantage
        > background check in companies
        > internet check for apps
        > configuration related checks before storing

    Self 

    self is the reference to the object created of our class
    it is passed whenever we are calling any functions
    only an object can access or helpful in connecting attributes and method inside our class

magic/dumber magic 

    start from __methodname__

    ex:
        __str__
        __add__

            creation>__int__ 
            print > __str
            + > __add__

Access Modifier 

    we can choose to provide access to our variables by maning there public or private
    normally we make all the data mumbers are privates

    variable or method are started with

        public   > available for all
        private __ > available inside class only
        protected _ > available for class and it childs

    we can also make our methods private as well

static method

    @staticmethod
    > methods belong to class not instance

Encapsulation :

    the binding of our data members/methods in a single unit is called as encapsulations

    > improve secruity
    > used getter and setter methods
    > used private variables

Inheritance :

    parent > child
    > gives us major advantages in code reusability

    we inherit :
        > non-private attributs
        > non-private methods
        > constructor [other magic methods]

    we can not access private attributes or methods of our parent class
    parent cant inherit from child but only child can inherit from parent

    super() > keyword is used to access methods of parent from our child class
        > cant be used outside
        > can only access methods and not attributes

    Types of Inheritance :
        simple          child > parent
        heirarichal     parent > child1,child2 [common parent]
        multilevel      grandparent > parent > child
        multiple        parent1 , parent 2 > child
        hybrid          mix of multiple inheritance

Polymorphism : 

    poly > multiple 
    moroh > shape.form

    in simple words , polymorphism is when a single entity can take multiple form

    > method overloading > by default not allowed in py just like java,C++
    > method overriding  > used in inheritance
    > operator overloading > used on operator

Abstraction : 

    abstract > abstract art > hidden

    > involve hiding complex implementation details and showing only essenital features
    > phone : make call , take call

    from abc import ABC , abstractmethod

    we have to ensure 2 things
        > inherit the abc class
        > should have an abstract methods

    so abstract classes are usful when we have a group of related objects that should share a commom features

    but should/will have different implementation

    > help in preparing a blurprint for other classes