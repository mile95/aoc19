import java.io.BufferedReader;
import java.io.FileReader;

public class day08 {

  private static final int w = 25;
  private static final int h = 6;

  private static String readInput() throws Exception {
    BufferedReader br = new BufferedReader(new FileReader("input.txt"));
    try {
      StringBuilder sb = new StringBuilder();
      String line = br.readLine();
      while (line != null) {
        sb.append(line);
        sb.append(System.lineSeparator());
        line = br.readLine();
      }
      return sb.toString();
    }
    finally {
      br.close();
    }
  }

  private static String solveA (String[] layers) {
    int indexLayerWithFewestZeros = 0;
    // Set it at max.
    int currentLowest = w*h;
    for(int i = 0; i < layers.length; i++) {
      int cand = layers[i].length() - layers[i].replace("0", "").length();
      if(cand < currentLowest) {
        currentLowest = cand;
        indexLayerWithFewestZeros = i;
      }
    }
    String finalLayer = layers[indexLayerWithFewestZeros];
    return ("PartA: " + (finalLayer.length()-finalLayer.replace("1","").length()) *
                        (finalLayer.length()-finalLayer.replace("2","").length()));
  }

  private static String solveB(String[] layers) {
    String finalImage = "";

    for(int i = 0; i < w*h; i++) {
      for(int k = 0; k < layers.length; k++) {
        if(layers[k].charAt(i) == '0' || layers[k].charAt(i) == '1') {
          finalImage += layers[k].charAt(i);
          break;
        }
      }
    }
    return finalImage;
  }

  public static void main(String[] args) throws Exception {

    String pixels = readInput();
    int numberOfLayers = pixels.length() / (w*h);
    String[] layers = new String[numberOfLayers];
    for(int i = 0; i < numberOfLayers; i++) {
      layers[i] = pixels.substring(i*w*h, i*w*h + w*h);
    }

    System.out.println(solveA(layers));
    String finalImage = solveB(layers);
    System.out.println("PartB: "); 
    for(int i = 0; i < h; i++) {
      System.out.println(finalImage.replace("0"," ").substring(i*w, i*w + w));
    }
  }
}
