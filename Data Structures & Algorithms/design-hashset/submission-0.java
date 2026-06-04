class MyHashSet {
    Map<Integer, Integer> hs;
    Integer timeT;
    public MyHashSet() {
        this.timeT=0;
        hs = new HashMap<>();
    }
    
    public void add(int key) {
        if (!hs.containsKey(key)) {
            hs.put(key, this.timeT+1);
        }
    }
    
    public void remove(int key) {
         if (hs.containsKey(key)) {
            hs.remove(key);
        }
    }
    
    public boolean contains(int key) {
        return hs.containsKey(key);
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */