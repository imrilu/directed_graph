package ex2;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Stack;

import com.google.gson.Gson;

public class DWGraph_Algo implements dw_graph_algorithms {
	private directed_weighted_graph dwg_alg;
	private HashMap<Integer,Double> d1;
	private HashMap<Integer,node_data> p1;
	
	/**
	 * Default constructor.
	 */
	public DWGraph_Algo() {
	}
	
	/**
	 * The constructor.
	 * @param g - the given graph.
	 */
	public DWGraph_Algo(directed_weighted_graph g) {
		dwg_alg = g;
	}
	
	/**
     * Init the graph on which this set of algorithms operates on.
     * @param g
     */
    public void init(directed_weighted_graph g) {
    	dwg_alg=g;
    }

    /**
     * Return the underlying graph of which this class works.
     * @return
     */
    public directed_weighted_graph getGraph() {
    	return dwg_alg;
    }
    
    /**
     * Compute a deep copy of this directed weighted graph.
     * @return
     */
    public directed_weighted_graph copy() {
    	directed_weighted_graph g  = new DWGraph_DS();
		for (node_data i : dwg_alg.getV()) {	
			g.addNode(i);
		}
		for (node_data i : dwg_alg.getV()) {
			int key = i.getKey(); 
			for (edge_data e : dwg_alg.getE(key)) {
				g.connect(key, e.getDest(),e.getWeight());
			}
		}
		return g;
    }
    
    /**
     * Compute the number of binding elements of the graph.
     * @param i
     * @param low_link
     * @param ids
     * @param OnStack
     * @param st
     * @param sccCount
     * @param id
     */
    public void SpecialDFS(int i, int low_link[],int ids[], boolean OnStack[], Stack<Integer> st, int sccCount,int id) {
    	st.push(i);
    	OnStack[i]=true;
    	ids[i]=id;
    	low_link[i]=id;
    	id++;
    	for(edge_data e : dwg_alg.getE(i)) {
    		if(ids[e.getDest()]==-1) {
    			SpecialDFS(e.getDest(),low_link,ids,OnStack,st, sccCount,id);
    		}
    		if(OnStack[e.getDest()]) {
    			low_link[i]=Math.min(low_link[i],low_link[e.getDest()]);
    		}
    	}
    	int w=-1;
		if(ids[i]==low_link[i]) {
			while(w!=i) {
				w=st.pop();
				OnStack[w]=false;
				low_link[w]=ids[i];
			}
			sccCount++;
		}
	}
    
    /**
     * Returns true if and only if (iff) there is a valid path from each node to each
     * other node. NOTE: assume directional graph (all n*(n-1) ordered pairs).
     * @return
     */
    public boolean isConnected() {
    	int ids [] = new int[dwg_alg.nodeSize()];
    	int low_link [] = new int[dwg_alg.nodeSize()];
    	boolean OnStack [] = new boolean[dwg_alg.nodeSize()];
    	Stack<Integer> st = new Stack<Integer>(); 
    	int sccCount=0;
    	int id =0;
    	for(int i=0;i<dwg_alg.nodeSize();i++) {
    		ids[i]=-1;
    		low_link[i]=-1;
    	}
    	for(int i=0;i<dwg_alg.nodeSize();i++) {
    		if(ids[i]==-1) {
    			SpecialDFS(i,low_link,ids,OnStack,st, sccCount,id);
    		}
    	}
    	if(sccCount==1) {
    		return true;
    	}
    	else {
    		return false;
    	}
    }
    
    /**
     * Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph.
     * @param s - the given source node.
     */
    public void Dijkstra(node_data s) {
    	d1 = new HashMap<Integer,Double>();
    	p1 = new HashMap<Integer,node_data>();
    	HashSet<Integer> visited = new HashSet<Integer>();
    	PriorityQueue<Node> q = new PriorityQueue<Node>(dwg_alg.nodeSize(), new Node());
    	for(node_data n : dwg_alg.getV()) {
    		d1.put(n.getKey(),Double.POSITIVE_INFINITY);
    		p1.put(n.getKey(),null);
    	}
    	d1.put(s.getKey(),(double) 0);
    	q.add(new Node(s.getKey(),0));
    	while(visited.size()!=dwg_alg.nodeSize()) {
    		int key = q.remove().key;
    		if(!visited.contains(key)) {
				for(edge_data v : dwg_alg.getE(key)) {
					if(!visited.contains(v.getDest())) {
		    			double sumDest=d1.get(key)+dwg_alg.getEdge(key, v.getDest()).getWeight();
		    			if(sumDest<d1.get(v.getDest())){
		    				d1.replace(v.getDest(),sumDest);
		    				p1.replace(v.getDest(), dwg_alg.getNode(key));
		    			}
		    			q.add(new Node(v.getDest(),d1.get(v.getDest())));
					}
				}
				visited.add(key);
    		}
    	}
    }
    
    /**
     * returns the length of the shortest path between src to dest.
     * Note: if no such path --> returns -1
     * @param src - start node
     * @param dest - end (target) node
     * @return
     */
    public double shortestPathDist(int src, int dest) {
    	Dijkstra(dwg_alg.getNode(src));
		return d1.get(dest);
    }
    /**
     * returns the the shortest path between src to dest - as an ordered List of nodes:
     * src--> n1-->n2-->...dest
     * see: https://en.wikipedia.org/wiki/Shortest_path_problem
     * Note if no such path --> returns null;
     * @param src - start node
     * @param dest - end (target) node
     * @return
     */
    public List<node_data> shortestPath(int src, int dest){
    	Dijkstra(dwg_alg.getNode(src));
		node_data s= dwg_alg.getNode(dest);
		List<node_data> list=new ArrayList<>();
		while(s!=null) {
			list.add(s);
			s=p1.get(s.getKey());	
		}
		Collections.reverse(list);
		return list;
    }

    /**
     * Saves this weighted (directed) graph to the given
     * file name - in JSON format
     * @param file - the file name (may include a relative path).
     * @return true - iff the file was successfully saved
     */
    public boolean save(String file) {
    	Gson gson = new Gson();
    	String json = gson.toJson(this.dwg_alg);
    	try {
    		PrintWriter pw = new PrintWriter(new File(file));
    		pw.write(json);
    		pw.close();
    		return true;
    	}
    	catch (FileNotFoundException e) {
    		e.printStackTrace();
    		return false;	
    	}
    }

    /**
     * This method load a graph to this graph algorithm.
     * if the file was successfully loaded - the underlying graph
     * of this class will be changed (to the loaded one), in case the
     * graph was not loaded the original graph should remain "as is".
     * @param file - file name of JSON file
     * @return true - iff the graph was successfully loaded.
     */
    public boolean load(String file) {
    	Gson gson =  new Gson();
    	try {
    		FileReader reader = new FileReader(file);
    		this.dwg_alg = gson.fromJson(reader, this.dwg_alg.getClass());
    		return true;
    	}
    	catch(FileNotFoundException e) {
    		e.printStackTrace();
    		return false;
    	}	
    }
}
/**
 * I created this Node class thats implements Comparator to fill the QriorityQueue by distance order.
 * @author Amitt
 */
class Node implements Comparator<Node> { 
    public int key;
    public double distance; 
  
    public Node() 
    { 
    } 
  
    public Node(int key, double distance) 
    { 
        this.key = key; 
        this.distance = distance; 
    } 
  
    @Override
    public int compare(Node node1, Node node2) 
    { 
        if (node1.distance < node2.distance) 
            return -1; 
        if (node1.distance > node2.distance) 
            return 1; 
        return 0; 
    } 
} 

