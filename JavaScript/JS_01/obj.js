function newObject(name, age) {
    var obj = new Object();
    obj.name = name;
    obj.age = age;
    return obj

}

function person(name, age) {
    this.name = name || '张无忌'; // this是当前对象。||表‘或’和默认值
    this.age = age || 20;
    this.setName = function (newName) {  //匿名函数，匿名对象
        this.name = newName;
    };
    this.getName = function () {
        return this.name;
    };
    return this;
}