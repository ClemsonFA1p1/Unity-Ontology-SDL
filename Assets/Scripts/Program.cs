using System;
using System.Net.Sockets;
using System.Text;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Linq;
using System.Globalization;

public class  Program : MonoBehaviour
{
    void Start()
    {
        try
        {
            TcpClient client = new TcpClient();
            client.Connect("localhost", 5000);
            NetworkStream stream = client.GetStream();
            int i =1;
            while (i!=0)
            {
            byte[] data = new byte[1024];
            int bytesRead = stream.Read(data, 0, data.Length);
            string message = Encoding.ASCII.GetString(data, 0, bytesRead);
            if (message==""){
                break;
            }
            // print(message);
            List<string> listItem= message.Split(' ').ToList();
            float X_l = float.Parse(listItem[1], CultureInfo.InvariantCulture.NumberFormat);
            float Y_l = float.Parse(listItem[2], CultureInfo.InvariantCulture.NumberFormat);
            Spawn(X_l,Y_l,listItem[0],listItem[3]);

            }
            stream.Close();
            client.Close();
        }
        catch (Exception ex)
        {
            Console.WriteLine("Exception: " + ex.Message);
        }
    }

    void Update()
    {
        

    }
    void Spawn(float x, float y, string Obstacles_name, string Obstacles_type)
    {
        string Link = "SDL_prefabs/";
        Vector3 pos=new Vector3(x,0,y);
        string file = Link + Obstacles_type;
        GameObject newObject = (GameObject)Instantiate(Resources.Load(file), pos,Quaternion.identity);
        newObject.name = Obstacles_name;

    }
}



