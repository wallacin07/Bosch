public class Main
 {
 public static void main(String[] args)
 {
 int[] array = new int[] {
 244, 232, 241, 123,
 232, 64, 111, 140
};

 int[] result = compact(array);
 for (int i = 0; i < result.length; i++){
System.out.printf("%d ", result[i]);
 }
 System.out.printf("\n");
 int[] descompacted = decompact(result);
 for (int i = 0; i < descompacted.length; i++)
System.out.printf("%d ", descompacted[i]);
 }

static int[] compact(int[] originalData)
 {
    int percorrer = 0;
     int[] binary = new int[originalData.length];
     int[] compact = new int[originalData.length/2];
     
    for (int i = 0; i < originalData.length; i++){
        binary[i] = originalData[i]>>4;
    }
    for (int i = 0; i < compact.length; i++){
        compact[i] = (binary[percorrer]<<4) + (binary[percorrer+1]);
        percorrer += 2;
    }
    return compact;
 }

static int[] decompact(int[] originalData){
     int percorrer = 0;
     int[] descompact = new int[originalData.length*2];
     for (int i = 0; i < originalData.length; i++) 
     {
        descompact[percorrer] = (originalData[i]&240)+6;
        percorrer++;
        descompact[percorrer] = ((originalData[i]&15)<<4)+6;
        percorrer++;
     }
     return descompact;
    }
     }
