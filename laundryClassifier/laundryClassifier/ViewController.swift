//
//  ViewController.swift
//  laundryClassifier
//
//  Created by Nikos Mouchtaris on 2/13/19.
//  Copyright © 2019 Nikos Mouchtaris. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        let url = URL(string: "http://127.0.0.1:5000/getLaundryState")!
        var request = URLRequest(url: url)
        request.httpMethod = "GET"
        NSURLConnection.sendAsynchronousRequest(request, queue: OperationQueue.main) {(response, data, error) in
            guard let data = data else { return }
            print(String(data: data, encoding: .utf8)!)
        }

    }
    

}

