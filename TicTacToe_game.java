package introduction.projects;
import java.util.Random;
import java.util.Scanner;
public class ticTacToe {
    static String a,b;
    static String[][] matrix=new String[3][3];
    static Scanner scan=new Scanner(System.in);
    static Random ran=new Random();
    public static void main(String[] args) {
        accessMatrix();
        System.out.println(".........TIC TAC TOE Game........");
        System.out.println("Enter the your wish X or O");
        a=scan.nextLine();
        b=null;
        if(a.equals("X")){
            b="O";
        }
        else if(a.equals("O")){
            b="X";
        }
        else{
            System.out.println("....invalid entry.... ");
        }
        System.out.println("then the computer wishes to be "+b);
        int count=0;
        while (true) {
            pro();
            System.out.println("enter the place in which the choice should be inserted");
            System.out.print("enter the place number");int d=scan.nextInt(9+1);
            switch (d) {
                case 1 -> matrix[0][0] = a;
                case 2 -> matrix[0][1] = a;
                case 3 -> matrix[0][2] = a;
                case 4 -> matrix[1][0] = a;
                case 5 -> matrix[1][1] = a;
                case 6 -> matrix[1][2] = a;
                case 7 -> matrix[2][0] = a;
                case 8 -> matrix[2][1] = a;
                case 9 -> matrix[2][2] = a;
            }
            count+=1;pro();
            while(true){
                int c=ran.nextInt(0,3);
                int e=ran.nextInt(0,3);
                if(matrix[c][e].equals("X")||matrix[c][e].equals("O")){
                  continue;
                }
                else{System.out.println("the computer choice is at the place "+"["+c+"]"+"["+e+"]");
                    matrix[c][e]=b;count+=1;break;}

            }
            if(winner().equals("wins")){
                    System.out.println("-------------the player "+a+" wins the game------------" +"\n"+
                            "............congratulation...........");break;
            }else if(winner().equals("compwins")){
                    System.out.println(".......the player"+b+" try again.......");break;
            }else {continue;
            }
        }
    }
    public static void pro(){
        for(int i=0;i<matrix.length;i++){
            for(int j=0;j<matrix[0].length;j++){
                System.out.print("|"+"  "+matrix[i][j]+"  "+"|");
            }
            System.out.println();
            System.out.println("---------------------");
        }
    }
    public static String winner(){
        String a1 ="nobody";
        //for diagonal
        if(matrix[0][0].equals(a)&&matrix[1][1].equals(a)&&matrix[2][2].equals(a)){a1="wins";}
        else if(matrix[0][0].equals(b)&&matrix[1][1].equals(b)&&matrix[2][2].equals(b)){a1="compwins";}
        else if(matrix[0][2].equals(a)&&matrix[1][1].equals(a)&&matrix[2][0].equals(a)){a1="wins";}
        else if(matrix[0][2].equals(b)&&matrix[1][1].equals(b)&&matrix[2][0].equals(b)){a1="compwins";}
        for(int i=0;i<matrix.length;i++){
            int countX1=0;
            int countO1=0;
            int countX2=0;
            int countO2=0;
            for(int j=0;j<matrix[0].length;j++){

                if(matrix[i][j].equals(a)){
                    countX1+=1;
                    if(countX1==matrix.length){a1="wins";}
                }
                if(matrix[i][j].equals(b)){countO1+=1;
                    if(countO1==matrix.length){a1="compwins";
                    }
                }
            }
            for(int k=0;k<matrix[i].length;k++){
                if(matrix[k][i].equals("O")||matrix[k][i].equals("X")){
                    if(matrix[k][i].equals(b)){
                        countO2+=1;
                        if(countO2==matrix.length) {
                            a1="compwins";break;}
                    }
                    if(matrix[k][i].equals(a)){countX2+=1;
                        if(countX2==matrix.length){a1="wins";break;}}
                }
            }
        }
        return a1;
    }
    public static void accessMatrix(){
        for(int i=0;i<matrix.length;i++){
            for(int j=0;j<matrix[0].length;j++){
                matrix[i][j]=" ";
            }
        }
    }
}
