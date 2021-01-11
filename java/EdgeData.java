package ex2;

public class EdgeData implements edge_data {
	private int src;
	private int dest;
	private double weight;
	private String info;
	private int tag;
	
	public EdgeData(int src,int dest, double weight) {	
		this.src=src;
		this.dest=dest;
		this.weight=weight;
	}
		
		/**
	 * The id of the source node of this edge.
	 * @return
	 */
	public int getSrc() {
		return this.src;
	}
	/**
	 * The id of the destination node of this edge
	 * @return
	 */
	public int getDest() {
		return this.dest;
	}
	/**
	 * @return the weight of this edge (positive value).
	 */
	public double getWeight() {
		return this.weight;
	}
	/**
	 * Returns the remark (meta data) associated with this edge.
	 * @return
	 */
	public String getInfo() {
		return this.info;
	}
	/**
	 * Allows changing the remark (meta data) associated with this edge.
	 * @param s
	 */
	public void setInfo(String s) {
		this.info=s;
	}
	/**
	 * Temporal data (aka color: e,g, white, gray, black) 
	 * which can be used be algorithms 
	 * @return
	 */
	public int getTag() {
		return this.tag;
	}
	/** 
	 * This method allows setting the "tag" value for temporal marking an edge - common
	 * practice for marking by algorithms.
	 * @param t - the new value of the tag
	 */
	public void setTag(int t) {
		this.tag=t;
	}
}


