import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Arrays;
import java.util.regex.*;

public class day12 {

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

  private static int compareInts(int a, int b) {
    if (a == b) {
      return 0;
    } else if (a > b) {
      return -1;
    } else {
      return 1;
    }
  }

  private static void partA(Moon[] moons) {

    for(int timestep = 0; timestep < 1000; timestep++) {

      // Update velocity of each moon by applying gravity
      for(int i = 0; i < moons.length - 1; i++) {
        for(int j = i + 1; j < moons.length; j++) {
            moons[i].xVel += compareInts(moons[i].xPos, moons[j].xPos);
            moons[i].yVel += compareInts(moons[i].yPos, moons[j].yPos);
            moons[i].zVel += compareInts(moons[i].zPos, moons[j].zPos);
            moons[j].xVel += compareInts(moons[j].xPos, moons[i].xPos);
            moons[j].yVel += compareInts(moons[j].yPos, moons[i].yPos);
            moons[j].zVel += compareInts(moons[j].zPos, moons[i].zPos);
        }
      }
      // Update positions of each moon by applying velocity
      for(Moon moon : moons) {
        moon.xPos += moon.xVel;
        moon.yPos += moon.yVel;
        moon.zPos += moon.zVel;
      }
    }

    for(Moon moon : moons) {
      moon.printMoon();
    }

    int totalE = 0;
    for(Moon moon : moons) {
      int potE = Math.abs(moon.xPos) + Math.abs(moon.yPos) + Math.abs(moon.zPos);
      int kinE = Math.abs(moon.xVel) + Math.abs(moon.yVel) + Math.abs(moon.zVel);
      totalE += potE * kinE;
    }
    System.out.println(totalE);

  }

  public static void main(String[] args) throws Exception {
    String[] lines = readInput().split("\\n");
    Moon[] moons = new Moon[4];
    for(int i = 0; i < lines.length; i++) {
      String[] values = lines[i].split(",");
      String x = values[0].split("x=")[1];
      String y = values[1].split("y=")[1];
      String z = values[2].split("z=")[1].replace(">","");
      moons[i] = new Moon(Integer.valueOf(x),Integer.valueOf(y), Integer.valueOf(z));
    }

    partA(moons);
  }

  private static class Moon {
    int xPos;
    int yPos;
    int zPos;
    int xVel;
    int yVel;
    int zVel;

    Moon(int xPos, int yPos, int zPos) {
      this.xPos = xPos;
      this.yPos = yPos;
      this.zPos = zPos;
      this.xVel = this.yVel = this.zVel = 0;

    }

    void printMoon() {
      System.out.println("Pos: " + xPos + "," + yPos + "," + zPos + " Vel: " + xVel + "," + yVel + "," + zVel);
    }
  }
}
