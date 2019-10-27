int main(void)
{
    int a = 3;
    int ret;
    ret = func1(a);  // func1() 호출
    return 0;
}
 
int func1(int num)
{
    int b;
    b = num + 2;
    func2(b);  // func2() 호출
    return;
}
 
void func2(int num)
{
  printf("func2");
}
