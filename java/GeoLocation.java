package ex2;

public class GeoLocation {
	private double x;
	private double y;
	private double z; 
	
	public double x() {
		return this.x;
	}
    public double y() {
    	return this.y;
    }
    public double z() {
    	return this.z;
    }
    public double distance(geo_location g) {
    	return Math.sqrt(Math.pow(g.x()-this.x, 2)+Math.pow(g.y()-this.y, 2)+Math.pow(g.z()-this.z, 2));
    }
}
