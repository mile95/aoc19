import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.lang.Math;
import java.util.Arrays;
import java.util.Collections;

public class day10 {

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

  public static double computeAngle(int[] ast1, int[] ast2) {
    int dx = ast1[0] - ast2[0];
    int dy = ast1[1] - ast2[1];
    return (270 + Math.toDegrees(Math.atan2(dy, dx)) + 360) % 360 ;
  }

  // Adds an asteriod at correct index. Increasing manhattan distance.
  public static ArrayList<int[]> addAsteriod(ArrayList<int[]> list, int[] asteriod, int[] center) {
    int distance = computeManhattanDistance(center,asteriod);
    int index = 0;
    for(int i = 0; i < list.size(); i++) {
      int distance2 = computeManhattanDistance(center,list.get(i));
      if(distance > distance2) {
        index++;
      } else {
        break;
      }
    }
    list.add(index, asteriod);
    return list;
  }

  public static int computeManhattanDistance(int[] center, int[] asteriod) {
    return Math.abs(asteriod[0] - center[0]) + Math.abs(asteriod[1]- center[1]);
  }

  public static int[] partA(ArrayList<int[]> asteroids) {

    int currentMax = 0;
    int[] currentBestLocation = new int[2];

    for(int i = 0; i < asteroids.size(); i++) {
      ArrayList<Double> degrees = new ArrayList<Double>();
      for(int j = 0; j < asteroids.size(); j++) {
        if(i != j) {
          Double angle = computeAngle(asteroids.get(i), asteroids.get(j));
          if(!degrees.contains(angle)) {
              degrees.add(angle);
          }
        }
      }
      if(degrees.size() > currentMax) {
        currentMax = degrees.size();
        currentBestLocation = asteroids.get(i);
      }
    }
    System.out.println("Part A: Location: " + Arrays.toString(currentBestLocation));
    System.out.println("Part A: Number: " + currentMax);
    return currentBestLocation;
  }

  public static void partB(int[] station, ArrayList<int[]> asteroids) {

    // Maps all degrees from the station to every asteriod with a list of asteriods.
    HashMap<Double, ArrayList<int[]>> map = new HashMap<Double,ArrayList<int[]>>();
    asteroids.remove(station);
    // Compute the angle from the station to all other asteriods and fill the map.
    for(int[] asteriod : asteroids) {
      Double angle = computeAngle(station, asteriod);
      if(!map.keySet().contains(angle)) {
        ArrayList<int[]> list = new ArrayList<int[]>();
        list.add(asteriod);
        map.put(angle, list);
      } else {
        ArrayList<int[]> list = map.get(angle);
        map.put(angle,addAsteriod(list,asteriod,station));
      }
    }

    // Sort all keys (degrees) in decresing order so we start from the correct position.
    ArrayList<Double> sortedKeys = new ArrayList<>(map.keySet());
    Collections.sort(sortedKeys);

    // Find the 200th removed asteriod! 
    int count = 0;
    while(count <=  200) {
      for(int i = 0; i < sortedKeys.size(); i++) {
        Double currentAngle = sortedKeys.get(i);
        if(!map.get(currentAngle).isEmpty()) {
          ArrayList<int[]> list = map.get(currentAngle);
          // The list is sorted in inc order (manhattan distance), removing the closest asteriod!
          int[] removedAsteroid = list.remove(0);
          map.put(currentAngle, list);
          count += 1;
          if(count == 200) {
            System.out.println("Part B: Asteriod: " + Arrays.toString(removedAsteroid));
            System.out.println("Part B: Value: " + (removedAsteroid[0] * 100 + removedAsteroid[1]));
          }
        }
      }
    }
  }

  public static void main(String[] args) throws Exception {
    String[] input = readInput().split("\\n");
    // Find all asteroids
    ArrayList<int[]> asteroids = new ArrayList<int[]>();
    for(int y = 0; y < input.length; y++) {
      for(int x = 0; x < input[y].length(); x++) {
        if(input[y].charAt(x) == '#') {
          asteroids.add(new int[]{x,y});
        }
      }
    }
    int[] station = partA(asteroids);
    partB(station, asteroids);
  }
}
