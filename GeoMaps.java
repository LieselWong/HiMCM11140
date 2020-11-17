/******************************************************************************
 *  Compilation:  javac GeoMaps.java
 *  Execution:    java GeoMaps n p
 *  Dependencies: StdDraw.java StdIn.java StdOut.java job_names.txt
 *
 *  Creates graphs that randomly generate the units, which will be converted into
 *  the conversion factor, and a table that has the coordinates and units.
 *
 ******************************************************************************/

import java.awt.Color;

public class GeoMaps{

  public static void main(String[] args) {

        //for a quicker calculation
        StdDraw.enableDoubleBuffering();

        //takes command in line inputs
        int n = Integer.parseInt(args[0]); //number of jobs we set
        int p = Integer.parseInt(args[1]); //number of people we are testing out

        //create array for the distance
        double[] dist = new double[n];

        //create array for job coordinates
        double[][] coo = new double[n][2];

        //set coordinate points in the coo array
        for (int i = 0; i < n; i++) {

          //generates the x and y for a job's coordinate point
          double x = ( (Math.random() * 6) + 2);
          double y = ( (Math.random() * 6) + 2);

          //assigning the elements of the array a coordinate point
          coo[i][0] = x;
          coo[i][1] = y;
        }

        //write names all in an array
        String[] name = StdIn.readAllLines();

        //for each person's trials
        for (int k = 0; k < p; k++) {

          //setting the scale of the graph.
          StdDraw.setXscale(0.0, 10.0);
          StdDraw.setYscale(0.0, 10.0);

          //to make the coordinate axes more visible
          StdDraw.setPenRadius(0.003);
          StdDraw.line(2.0, 2.0, 2.0, 8.0);
          StdDraw.line(2.0, 2.0, 8.0, 2.0);

          //put circles on the end of the coordinate axes
          StdDraw.setPenRadius(0.009);
          StdDraw.point(8.0, 2.0);
          StdDraw.point(2.0, 2.0);
          StdDraw.point(2.0, 8.0);

          //dashes across the coordinate axes
          for (double i = 3.0; i < 9.00; i++){
            StdDraw.setPenRadius(0.001);
            StdDraw.setPenColor(new Color(0, 0, 0));
            if (i < 8.00){
              StdDraw.line(i, 1.75, i, 8.00);
              StdDraw.line(1.75, i, 8.00, i);
            }
            else{
              StdDraw.line(i, 2.00, i, 8.00);
              StdDraw.line(2.00, i, 8.00, i);
            }
          }


          //prints out chart for the diagram
            System.out.println("Person: " + k);
            System.out.printf("%1s %60s %30s%n", "Job Name", "Coordinate Points", "Units");
            System.out.print("--------------------------------------------------------");
            System.out.println("------------------------------------------------------");

          //generates the person's points
            StdDraw.setPenRadius(0.005);
            StdDraw.setPenColor(new Color(255, 0, 0));
            double z = ((Math.random() * 6) + 2);
            double m = ((Math.random() * 6) + 2);
            StdDraw.point(z, m);

          //sets the pen color to random color
            int color1 = ((int)(Math.random() * 256));
            int color2 = ((int)(Math.random() * 256));
            int color3 = ((int)(Math.random() * 256));
            StdDraw.setPenColor(new Color(color1, color2, color3));

        //finds distance and prints distance, coordinates, and name of job
         for (int i = 0; i < n; i++) {

          StdDraw.setPenRadius(0.0009);

          //prints the name of the job
          System.out.printf("%1s", name[i]);

          //prints the coordinate points
          //System.out.print("                         " + "(" + x1 + ", " + y1 + ")");
          System.out.printf("%12s %.4f %s %4.4f %s", "(", coo[i][0], ",", coo[i][1], ")");

          //draws the line between the applicant's house and the job's workplace
          StdDraw.line(coo[i][0], coo[i][1], z, m);

          //calculates the length of the line
          dist[i] = Math.sqrt(Math.pow((coo[i][0] - z), 2) + Math.pow((coo[i][1] - m), 2));

          //prints the distance between coordinate points
          System.out.printf("%30.4f%n", dist[i]);
        }

        for (int i = 0; i < n; i++) {
          //sets the pen color to black
          StdDraw.setPenColor(new Color(0, 0, 0));

          //sets the pen radius smaller to make it look neat
          StdDraw.setPenRadius(0.003);

          //draws the randomly generated point
          StdDraw.point(coo[i][0], coo[i][1]);
        }
        // display all of the points now
        StdDraw.show();
        System.out.println();
        StdDraw.save(String.valueOf(k) + ".png");
        StdDraw.clear();
      }

  }
}
