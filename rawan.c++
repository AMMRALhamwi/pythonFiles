#include <iostream>
using namespace std;
int main ()
{float netsalary,salary,tax,socialinsurance;
cin>>salary;
socialinsurance=salary*7/100;
netsalary=salary-(tax+socialinsurance);
cout<<"social insurance are"<<socialinsurance<<endl;
if (salary>=185940 && salary<=250000){
    tax=salary*5/100;
    cout<<"tax is"<<tax<<endl;
    cout<<"net salary is "<<netsalary<<endl;
}


}