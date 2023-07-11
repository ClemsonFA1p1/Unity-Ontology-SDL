using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Zaxis_set : MonoBehaviour
{
    void Start()
    {
        transform.position = new Vector3(transform.position.x, /*y*/Terrain.activeTerrain.SampleHeight(transform.position) + 0.033f /*y*/, transform.position.z);
    }

    void Update()
    {
        

    }
}