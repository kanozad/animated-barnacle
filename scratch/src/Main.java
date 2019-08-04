public class Main {

    public static void main(String[] args) {
        System.out.println("Hello World!");

        System.out.println(boof("201805"));
        System.out.println(boof("203X01"));
        System.out.println(boof(null));

        System.out.println((String)null);
    }

    static String boof(String in) {
        if(in == null) return null;

        if(in.length() != 6) return in;

        return in.substring(4) + "/" + in.substring(0,4);
    }
}
