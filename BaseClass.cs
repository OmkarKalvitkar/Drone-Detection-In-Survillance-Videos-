class BaseClass
{
    protected int i = 13;
}
class Derived: BaseClass
{
    int i = 9; 
    public void fun()
    {
        Console.WriteLine(i + "" +base.i);
    } 
}
