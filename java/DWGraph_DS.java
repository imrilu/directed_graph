package ex2;

import java.util.Collection;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;

public class DWGraph_DS implements directed_weighted_graph {
	private HashMap<Integer,node_data> nodes;
	private int NumofEdges;
	private int ModeCount;
	
	public class NodeData implements node_data {
		private int key;
		private double weight;
		private String info;
		private int tag;
		private GeoLocation gl;
		private HashMap<Integer,edge_data> out_edges;
		private HashSet<Integer> in_edges;
		
		/**
		 * The constructor.
		 * @param key - given.
		 */
		public NodeData(int key) {
			this.key=key;
			out_edges=new HashMap<Integer,edge_data>();
		}
		
		/**
		 * This method returns a collection with all the out edges of this node_data */
		public Collection<edge_data> getNi_out(){
			return out_edges.values();
		}
		
		/**
		 * This method returns a HashSet with all the in edges of this node_data */
		public HashSet<Integer> getNi_in(){
			return in_edges;
		}
		
		/**
		 * This method returns a specific edge of this node_data */
		public edge_data getNiEdge(int dest){
			return out_edges.get(dest);
		}
		
		
		/** This method adds the out_edge to this node_data.*/
		public void addNi_out(int dest, double w) {
			EdgeData edge=new EdgeData(this.key,dest,w);
			out_edges.put(dest,edge);
		}
		
		/** This method adds the in_edge to this node_data.*/
		public void addNi_in(int src) {
			in_edges.add(src);
		}
		
		/**
		 * return true iff this<==>key are adjacent, as an edge between them.
		 * @param key- the given dest.
		 * @return boolean.
		 */
		public boolean hasNi_out(int dest) {
			if ((!(out_edges.isEmpty())) && (out_edges.containsKey(dest)))
				return true;
			else
				return false;	
		}
		
		/**
		 * Removes the edge of this-key.
		 * @param key - the given key.
		 */
		public edge_data removeEdge_out(int key) {
			edge_data e = null;
			if(out_edges.containsKey(key)) {
				e = out_edges.get(key);
				out_edges.remove(key);
			}
			return e;
		}
		
		/**
		 * Removes the edge this-key.
		 * @param key - the given key.
		 */
		public void removeEdge_in(int key) {
			if(in_edges.contains(key)) {
				in_edges.remove(key);
			}
		}
		
		/**
		 * Returns the key (id) associated with this node.
		 * @return
		 */
		public int getKey() {
			return this.key;
		}
		
		/** Returns the location of this node, if
		 * none return null.
		 * 
		 * @return
		 */
		public geo_location getLocation() {
			return (geo_location) gl;
		}
		
		/** Allows changing this node's location.
		 * @param p - new new location  (position) of this node.
		 */
		public void setLocation(geo_location p) {
			this.gl=(GeoLocation) p;
		}
		
		/**
		 * Returns the weight associated with this node.
		 * @return
		 */
		public double getWeight() {
			return this.weight;
		}
		
		/** 
		 * Allows changing this node's weight.
		 * @param w - the new weight
		 */
		public void setWeight(double w) {
			this.weight=w;
		}
		
		/**
		 * Returns the remark (meta data) associated with this node.
		 * @return
		 */
		public String getInfo() {
			return this.info;
		}
		
		/**
		 * Allows changing the remark (meta data) associated with this node.
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
		 * Allows setting the "tag" value for temporal marking an node - common
		 * practice for marking by algorithms.
		 * @param t - the new value of the tag
		 */
		public void setTag(int t) {
			this.tag=t;
		}
		
		/**
	     * equals function - return true if the two object are equals.
	     * else, return false.
	     */
	    public boolean equals(Object o) {
	    	if (key !=((NodeData)o).key)
	    		return false;
	    	for (int i: out_edges.keySet())
	    	{
	    		if (!((NodeData)o).out_edges.containsKey(i))
	    			return false;
	    		if (!((NodeData)o).out_edges.get(i).equals(out_edges.get(i)))
	    			return false;
	    	}
	    	return true;
	    }
	
	}
	
	/**
	 * The constructor.
	 */
	public DWGraph_DS() {
		nodes=new HashMap<Integer,node_data>();
		NumofEdges=0;
		ModeCount=0;
	}
	
	/**
	 * returns the node_data by the key.
	 * @param key - the key
	 * @return the node_data by the key, null if none.
	 */
	public node_data getNode(int key) {
		if(!nodes.containsKey(key)) { 
			return null;
		}
		else {
			return nodes.get(key);
		}		
	}
	
	/**
	 * returns the data of the edge (src,dest), null if none.
	 * Note: this method should run in O(1) time.
	 * @param src
	 * @param dest
	 * @return
	 */
	public edge_data getEdge(int src, int dest) {
		return ((NodeData)(nodes.get(src))).getNiEdge(dest);
	}
	
	/**
	 * adds a new node to the graph with the given node_data.
	 * Note: this method should run in O(1) time.
	 * @param n
	 */
	public void addNode(node_data n) {
		if (!nodes.containsKey(n.getKey())) {
    		nodes.put(n.getKey(), n);
    		ModeCount++;	
    	}
	}
	
	/**
     * return true iff (if and only if) there is an edge between src and dest
     * Note: this method should run in O(1) time.
     * @param src
     * @param dest
     * @return
     */
    public boolean hasEdge(int src, int dest) {
    	return ((NodeData)nodes.get(src)).hasNi_out(dest);
    }
	
/**
 * Connects an edge with weight w between node src to node dest.
 * * Note: this method should run in O(1) time.
 * @param src - the source of the edge.
 * @param dest - the destination of the edge.
 * @param w - positive weight representing the cost (aka time, price, etc) between src-->dest.
 */
	public void connect(int src, int dest, double w) {
		if(!hasEdge(src,dest) && (src!=dest)) {
    		((NodeData)nodes.get(src)).addNi_out(dest,w);
    		((NodeData)nodes.get(dest)).addNi_in(src);
			NumofEdges++;
			ModeCount++;	
    	}
	}
	/**
	 * This method returns a pointer (shallow copy) for the
	 * collection representing all the nodes in the graph. 
	 * Note: this method should run in O(1) time.
	 * @return Collection<node_data>
	 */
	public Collection<node_data> getV(){
		return nodes.values();	
	}
	
	/**
	 * This method returns a pointer (shallow copy) for the
	 * collection representing all the edges getting out of 
	 * the given node (all the edges starting (source) at the given node). 
	 * Note: this method should run in O(k) time, k being the collection size.
	 * @return Collection<edge_data>
	 */
	public Collection<edge_data> getE(int node_id){
		return ((NodeData)(nodes.get(node_id))).getNi_out();
	}
	
	/**
	 * Deletes the node (with the given ID) from the graph -
	 * and removes all edges which starts or ends at this node.
	 * This method should run in O(k), V.degree=k, as all the edges should be removed.
	 * @return the data of the removed node (null if none). 
	 * @param key
	 */
	public node_data removeNode(int key) {
		if(getNode(key)!=null) {
			HashSet<Integer> in_edges = ((NodeData)(nodes.get(key))).getNi_in();
			Iterator<Integer> i = in_edges.iterator();  
	        while(i.hasNext())  {  
	        	((NodeData)(nodes.get(i))).removeEdge_out(key);
				NumofEdges--;
				ModeCount++;
	        }  
	        node_data n = nodes.get(key);
			nodes.remove(key);
			return n;
		}
		else
			return null;	
	}
	
	/**
	 * Deletes the edge from the graph.
	 * Note: this method should run in O(1) time.
	 * @param src
	 * @param dest
	 * @return the data of the removed edge (null if none).
	 */
	public edge_data removeEdge(int src, int dest) {
		edge_data e = null;
		if(hasEdge(src,dest)) {
        	e = ((NodeData)nodes.get(src)).removeEdge_out(dest);
        	((NodeData)nodes.get(dest)).removeEdge_in(src);
        	NumofEdges--;
        	ModeCount++;
    	}	
		return e;
	}
	
	/** Returns the number of vertices (nodes) in the graph.
	 * Note: this method should run in O(1) time. 
	 * @return
	 */
	public int nodeSize() {
		return nodes.size();
	}
	
	/** 
	 * Returns the number of edges (assume directional graph).
	 * Note: this method should run in O(1) time.
	 * @return
	 */
	public int edgeSize() {
		return NumofEdges;
	}
	
	/**
	 * Returns the Mode Count - for testing changes in the graph.
	 * @return
	 */
	public int getMC() {
		return ModeCount;
	}
	
	 /**
     * equals function - return true if the two object are equals.
     * else, return false.
     */
    public boolean equals(Object o) {
    	if (nodes.size()!=((DWGraph_DS)o).nodes.size())
    		return false;
    	for (int i: nodes.keySet()){
    		if (!((DWGraph_DS)o).nodes.containsKey(i))
				return false;
    		if (!((NodeData)nodes.get(i)).equals((NodeData)((DWGraph_DS)o).nodes.get(i)))
    			return false;
    	}
    	return true;
    }
}

